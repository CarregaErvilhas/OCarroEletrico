# Shared CI workflows

This repo hosts the group's shared CI. Each rule has one copy here; the other repos call it.

| Workflow | What it does | Used here |
| --- | --- | --- |
| `.github/workflows/indexnow.yml` | Submits a site's sitemap to IndexNow after a deploy | `pages.yml` |
| `.github/workflows/dco-check.yml` | Fails a pull request with a commit lacking a matching `Signed-off-by` | `dco.yml` |
| `.github/workflows/cla.yml` | CLA signature check with CLA Assistant Lite | no (this repo uses the DCO) |

Callers in other repos pin a full commit SHA, like any action:

```yaml
uses: CarregaErvilhas/OCarroEletrico/.github/workflows/<file>@<sha> # main
```

A change here reaches a caller only when its pin moves.

A called job reports its check as `<caller job id> / <called job id>`. Renaming a job id breaks any ruleset that requires the check, and moving a repo from its own job to a caller changes the name too: update the ruleset in the same step.

## IndexNow

| Input | Required | Meaning |
| --- | --- | --- |
| `host` | yes | Host without scheme. `https://<host>/sitemap.xml` lists the URLs |
| `key` | yes | IndexNow key, published at `https://<host>/<key>.txt`. Not a secret |

The job never fails the run. The caller chooses when it runs:

```yaml
  indexnow:
    needs: deploy
    if: github.event_name == 'push'
    uses: CarregaErvilhas/OCarroEletrico/.github/workflows/indexnow.yml@<sha> # main
    with:
      host: <host>
      key: <key>
```

## DCO

No inputs. The caller is the whole `.github/workflows/dco.yml`:

```yaml
name: DCO
on: pull_request
permissions:
  contents: read
jobs:
  dco:
    uses: CarregaErvilhas/OCarroEletrico/.github/workflows/dco-check.yml@<sha> # main
```

The check name is `dco / dco`.

The script comes from this repo, never from the caller's checkout, so a pull request can't edit the rule that checks it. The workflow reads its own source from `job.workflow_repository` and `job.workflow_sha`, so the script is the one at the pinned SHA. `github.workflow_sha` would not do: in a called workflow, the `github` context belongs to the caller. The run fails if either value is empty, and the log prints the source used.

This repo calls the workflow by local path, which resolves to the pull request's own merge commit. For that case only, the script is taken from the pull request's base commit.

A `pull_request` run still reads the caller's workflow files from the pull request, so changes under `.github/` need review.

A caller's local `scripts/check-dco.sh`, if kept for use before pushing, is not what CI runs.

## CLA

| Input | Required | Default | Meaning |
| --- | --- | --- | --- |
| `document-url` | yes | | URL of the CLA |
| `sign-comment` | yes | | Exact comment that signs it, as written in the CLA |
| `notsigned-comment` | yes | | Posted when an author hasn't signed |
| `allsigned-comment` | yes | | Posted when every author has signed |
| `allowlist` | yes | | Comma-separated logins that don't sign |
| `signatures-path` | no | `signatures/v1/cla.json` | Bump the version when the terms change |
| `branch` | no | `cla-signatures` | Branch of the caller's repo that holds the signatures |

The only token is the caller's `GITHUB_TOKEN`, which the called workflow receives by itself: pass no secrets. The caller must declare both triggers, grant the permissions (a called workflow can't raise them), and keep `name: CLA`, which the action uses to rerun the check after a signing comment.

```yaml
name: CLA
on:
  issue_comment:
    types: [created]
  pull_request_target:
    types: [opened, synchronize, reopened, closed]
permissions:
  actions: write
  contents: write
  pull-requests: write
  statuses: write
jobs:
  cla:
    uses: CarregaErvilhas/OCarroEletrico/.github/workflows/cla.yml@<sha> # main
    with:
      document-url: https://github.com/CarregaErvilhas/<repo>/blob/main/CLA.md
      sign-comment: <sentence from CLA.md>
      notsigned-comment: <text>
      allsigned-comment: <text>
      allowlist: <maintainer-login>,*[bot]
```

`pull_request_target` runs with write permissions even for forks. Neither the caller nor `cla.yml` may check out or run the pull request's code.
