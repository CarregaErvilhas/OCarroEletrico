# How a Zerops service is exposed

The group's one copy of this procedure. Each repo documents only its own service (ports, readiness path, user name, timeouts) and links here. Zone-wide Cloudflare rules are in [cloudflare-zone.md](cloudflare-zone.md).

A service without a public route (a collector, a worker) only needs [Non-root process](#non-root-process) and [Readiness and health checks](#readiness-and-health-checks).

```
client ──► Cloudflare (proxy, TLS) ──► Zerops L7 balancer ──► service
```

## The rules

- **One `AAAA` record** per domain, to the project's dedicated IPv6, **proxy on**. No `A` record.
- **Access Policy on the balancer**: default deny, only Cloudflare's ranges.
- **Let's Encrypt certificate** issued by Zerops on the balancer.
- **No `zerops.app` subdomain** in production: it goes around Cloudflare.
- **The origin IP is never written in a repo.** Read it from the Zerops console, the Cloudflare record or the API (see [Tools](#tools)).

## Why `AAAA` only

Zerops' shared IPv4 finds the project by looking at the domain's `AAAA`. With the Cloudflare proxy on, that `AAAA` is Cloudflare's, so routing fails: a proxied `A` to the shared IPv4 doesn't work, and Zerops' own docs say not to use it. With the proxy on and an IPv6-only origin, Cloudflare translates, and IPv4 clients reach the same origin.

The CNAME that Zerops also offers adds nothing: with the shared IPv4 excluded it points to the same IPv6, and that switch applies to the whole project.

## Add a domain (the order matters)

Two records in two systems, Zerops first. The API calls below can also be done in the Zerops console.

**1. Zerops: register the domain on the balancer**, with SSL on. Without this the balancer answers **404** to any `Host` it doesn't know.

If the project has no routing yet:

```
POST /api/rest/public/project/<project-id>/public-http-routing
{
  "domains": ["<domain>"],
  "locations": [{ "path": "/", "port": <port>, "serviceStackId": "<service-id>" }],
  "sslEnabled": true,
  "cdnEnabled": false
}
```

To add a domain to an existing routing, use that routing's `PUT` (a `POST` fails with `publicHttpRoutingDuplicateDomainNameInAnotherRouting`):

```
PUT /api/rest/public/public-http-routing/<routing-id>
{ "domains": [...], "locations": [...], "sslEnabled": true, "cdnEnabled": false }
```

Copy `locations` as it is: the Access Policy lives there. After the `PUT` the routing is `isSynced: false` and takes effect only after `PUT /api/rest/public/project/<project-id>/sync-public-http-routing` (no body). Without the sync the new domain keeps answering 404.

At this point `dnsCheckStatus` is `PENDING` and `sslStatus` is `WAITING_FOR_DNS`: Zerops waits for DNS before issuing the certificate.

**2. Cloudflare: the DNS record.**

```
<domain>  AAAA  <project IPv6>  proxy: ON
```

**3. Zerops: check the DNS.** `PUT /api/rest/public/public-http-routing/<routing-id>/trigger-domains-dns-check` with `{"domains": [...]}`. The status becomes `dnsCheckStatus: OK` and the certificate follows (`sslStatus: ACTIVE`).

Then set the [Access Policy](#access-policy) and [verify](#verify).

The zone settings Zerops needs are in [cloudflare-zone.md](cloudflare-zone.md#tls-and-https). If the certificate isn't issued because Cloudflare forces HTTPS on the HTTP-01 challenge, add a Cloudflare Configuration Rule that turns off *Automatic HTTPS Rewrites* on `/.well-known/acme-challenge/`.

## Access Policy

Hiding the IP is an extra layer. The defence is the balancer's Access Policy: if the IP leaks, a direct request is refused. It checks the address of whoever connects to the balancer, which is Cloudflare.

Set it in the console (the domain's settings → *Access Policy*: *Default Policy* `deny`, *CIDR Blocks* = Cloudflare's ranges, one per line) or through the routing API. `zerops.yml` and `zcli` have no setting for it.

```json
"config": {
  "accessPolicy": {
    "enabled": true,
    "defaultPolicy": "deny",
    "cidr": ["<Cloudflare IPv4 ranges>", "<Cloudflare IPv6 ranges>"]
  }
}
```

- **Leave `setRealIpFrom` empty.** With Cloudflare's ranges in it, the balancer replaces the connecting address with the user's IP (from the forwarded header). That IP isn't Cloudflare's, so every request gets 403.
- The ranges are at <https://www.cloudflare.com/ips-v4> and <https://www.cloudflare.com/ips-v6>. They change now and then: **review them and update by hand.**
- A wrong policy also cuts legitimate traffic. After any change, check that the site answers 200.

## Verify

```bash
# straight to the origin, without Cloudflare: must be 403
curl -s -o /dev/null -w '%{http_code}\n' --resolve "<domain>:443:[$ORIGIN_IPV6]" https://<domain>/<readiness-path>
# through Cloudflare: must be 200
curl -s -o /dev/null -w '%{http_code}\n' https://<domain>/<readiness-path>
```

Run the first one from a machine with IPv6, outside Cloudflare. Reading the answers:

| Code | Meaning |
| --- | --- |
| 200 | Through Cloudflare: fine. Direct to the origin: **the Access Policy isn't applied** |
| 403 | The Access Policy refused the request. Expected when direct |
| 404 | The domain isn't registered (or synced) on the balancer |
| 502 | Certificate or origin problem |

If the direct request fails on the certificate, add `-k` while you diagnose.

## Behind the two proxies

- **Client IP.** Cloudflare appends the client's IP to `X-Forwarded-For` (and sends `CF-Connecting-IP`); the balancer appends the address that connected to it. With the Access Policy as above, the client's entry is the second from the right. Only trust it while the policy is on: without it, anyone who reaches the origin writes whatever header they like. A per-IP limit built on the wrong entry puts every visitor in one counter, so test it from two networks.
- **Other `X-Forwarded-*` headers.** The balancer sets `Host`, `Proto` and `Port`, but sends `X-Forwarded-Port: 80` even on HTTPS, and passes the client's `X-Forwarded-Prefix` through. Cloudflare adds no `X-Forwarded-Host`. If your app builds absolute URLs from these, trust only the headers you checked.
- **Upload size.** A Zerops custom domain cuts requests above 512 MB, and the Cloudflare proxy has its own lower limit ([cloudflare-zone.md](cloudflare-zone.md#proxy-limits)).

## Non-root process

Zerops' default user (`zerops`) has sudo, so code running in the process would be root in the container. Create a user with no sudo, no shell and no home in `run.prepareCommands`, and start the process as it.

Alpine (BusyBox `adduser`):

```yaml
run:
  base: alpine/nodejs@24
  prepareCommands:
    - sudo addgroup -S <app-user>
    - sudo adduser -S -D -H -s /sbin/nologin -G <app-user> <app-user>
  startCommands:
    - command: node src/server.js
      name: <name>
      workingDir: /var/www
      user: <app-user>
```

Ubuntu:

```yaml
  prepareCommands:
    - sudo useradd --system --no-create-home --shell /usr/sbin/nologin <app-user>
```

- **Same libc in build and run** when a native module is picked at install time.
- The user reads the code in `/var/www` (owned by `zerops`) but can't write it. It writes in `/tmp`: point caches and `HOME` there if something needs them. Anything installed outside `/var/www` must be readable by it (Ubuntu creates home directories as `0750`).
- `run.start` runs without a shell, so `cd dir && …` fails: use `startCommands` with `workingDir`. Where `startCommands` do go through a shell (seen on Ubuntu), quote shell characters.
- **Owner credentials stay out of the process.** Work that needs them (database owner or superuser) runs in `initCommands`, and the start command strips the variable: `env -u <VARIABLE> <command>`.
- This doesn't hide the secrets the app does use: they're in its environment. It stops code changes, installs and root.
- `prepareCommands` are cached. A redeploy alone doesn't rebuild that image: after clearing the runtime prepare cache, deploy again and check the user.

After a deploy that touches this, in the container's terminal:

```bash
ps -o user,pid,args | grep <process-name>    # Alpine (BusyBox ps has no -C): user = <app-user>
ps -eo user,pid,args | grep <process-name>   # Ubuntu
```

## Readiness and health checks

- **`deploy.readinessCheck` gates traffic.** A new container takes traffic only after it passes. If it doesn't pass within `failureTimeout`, the deploy fails and, with a rolling deploy, the previous version keeps serving.
- **`run.healthCheck` is liveness**, and runs all the time. Don't make it depend on a database or another service: with one container, a blip would take the whole site down.
- Both run from inside the container, without authentication. A route behind auth answers 401 and marks the service broken for good. Codes in `[200, 400)` pass.
- A readiness route anyone can reach shouldn't do expensive work for outside callers.
- **Rolling (`temporaryShutdown: false`)** when two containers can run at once: allow `maxContainers: 2`, and the second exists only during a deploy. **Stop-first (`true`)** when the service must be unique: the deploy has a gap.
- The timeout must outlast boot (recovery, migrations, downloads).
- Before activating an older app version in the console, check that it has the readiness path now configured: a version without the route never becomes ready.

Zerops docs: <https://docs.zerops.io/guides/readiness-health-checks> and <https://docs.zerops.io/guides/deployment-lifecycle>.

## Tools

The API host depends on the region (`https://api.app-<region>.zerops.io/api/rest/public`). The token is the one `zcli login` stores; on macOS:

```bash
TOKEN=$(python3 -c "import json;print(json.load(open('$HOME/Library/Application Support/zerops/cli.data'))['LoginSession']['AccessToken'])")
API=https://api.app-<region>.zerops.io/api/rest/public
# routings
curl -s -H "Authorization: Bearer $TOKEN" "$API/project/<project-id>/public-http-routing"
# the origin IPv6
curl -s -H "Authorization: Bearer $TOKEN" "$API/project/<project-id>" | python3 -c "import sys,json;print(json.load(sys.stdin)['publicIpV6'])"
```

Never print the token, and never commit it or the IP. The full API spec is at `$API/swagger/openapi.yml`. Project and service IDs: `zcli project list`, `zcli service list -P <project-id>`.
