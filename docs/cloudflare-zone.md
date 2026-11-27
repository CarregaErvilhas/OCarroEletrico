# Cloudflare: zone-wide rules

`ocarroeletrico.com` is one Cloudflare zone on the **Free plan**, shared by several projects. A change here can break a service you aren't working on, so read this before touching zone settings, DNS, WAF, cache or redirect rules, whichever repo you're in.

This file says what each rule is for and who depends on it. The dashboard owns the numbers and values. Update this file in the same change as a rule. How a Zerops service sits behind the zone: [zerops-exposure.md](zerops-exposure.md).

## TLS and HTTPS

- SSL mode **Full (strict)**, **IPv6** on and **Always Use HTTPS** on: Zerops origins need the first two.
- **Minimum TLS** for the zone is 1.2, with 1.3 on.
- The **R2 custom domains** (`pictures.*`, `maptiles.*`, `ohm-age.*`) require **TLS 1.3**. Older clients can't connect to them. The setting is per custom domain, not the zone's.
- Cloudflare adds **HSTS** with `includeSubDomains` and preload, so every subdomain is committed to HTTPS.
- No Configuration Rules are in use.

The second zone (CEME's OMIE statistics domain) has its own settings and isn't covered here.

## Page features

*Email Address Obfuscation*, *Rocket Loader* and Bot Fight Mode are off. A feature that injects scripts into pages can be blocked by a service's Content Security Policy: check the pages of every proxied service before turning one on.

## Rate limiting: the only rule

The Free plan allows **one** rate limiting rule, and it's taken: a flood guard for ohmigo's MCP server.

- It matches the path **`/mcp` on every host of the zone**, any method, so it also covers any other `/mcp` behind the proxy (olh'o'posto's).
- It blocks for a short while an IP that floods it, counted per Cloudflare data center.
- It's a flood guard, not a quota. It's set high on purpose: a whole assistant platform arrives from few addresses. Don't lower it.
- A deploy doesn't change it.

Anything else that needs a limit does it in its own code (for a Worker, the rate limiting binding).

## WAF custom rules

| Protects | What it does | If it's lost | Owner's setup and checks |
| --- | --- | --- | --- |
| AmpereArchive's public host (`ohm-age.*`) | Blocks every path outside `/v1/`. An R2 custom domain exposes the whole bucket | Private state and raw data become public | `Docs/deploy.md` in AmpereArchive (private repo) |
| Panoramax reports (`panoramax.*`) | Blocks `POST` on the reports API unless the request carries the header the olh'o'posto Worker sends | Anyone can hide any photo with a script | [OlhaOPosto `Docs/cloudflare.md`](https://github.com/CarregaErvilhas/OlhaOPosto/blob/main/Docs/cloudflare.md), *Pedidos de remoção* |

After any change to the zone, run the owner's checks.

DDoS protection is in front of everything proxied.

## Cache rules

| Host and paths | What it does | Why |
| --- | --- | --- |
| `ohmigo.*`, `/dados` and its JSON files | Cached, TTLs from the origin's `Cache-Control` | Cloudflare doesn't cache HTML or JSON without a rule |
| `pictures.*` | Long edge TTL, 4xx and 5xx not cached, query string out of the key | The olh'o'posto Worker purges on change |
| `panoramax.*`, picture files (`/api/pictures/….jpg`) | Origin TTLs, 4xx never stored | A hidden photo answers 404 until approved |
| `panoramax.*`, everything else | Never cached | Panoramax marks API, tiles and pages as `public` |
| `maptiles.*`, except `current.json` | Long edge TTL, shorter browser TTL, 4xx not cached, query string out of the key | Files never change in place; `current.json` is the pointer |

## Redirect rules

Single redirects send a few old or convenience subdomains (OMIE data, operator list, simulators, the old CEME name) elsewhere. Their targets are in the dashboard.

## Proxy limits

The proxy caps the size of a request body according to the plan, below Zerops' own cap. Check Cloudflare's current Free limit before accepting large uploads through a proxied host.

## Which CLI manages what

| What | Tool |
| --- | --- |
| Zone and account resources: R2, custom domains, DNS, Cache Rules, purges | `cf` |
| A Worker, its D1 database and its secrets | `wrangler`, through the owning repo's npm scripts. Don't run `cf dev`, `cf deploy` or `cf migrate` on such a project ([why](https://github.com/CarregaErvilhas/OlhaOPosto/blob/main/Docs/cloudflare.md)) |
| WAF custom rules and the rate limiting rule | Dashboard: *Security → WAF* |
| Zerops services | `zcli` and the console ([zerops-exposure.md](zerops-exposure.md)) |

In `cf`, commands that delete or replace need `--force` without an interactive terminal.

## Check what's live

Look at the dashboard, or read the zone's rulesets through the API with a read-only token. WAF expressions can contain a secret header value: don't paste them into an issue, a log or a chat.
