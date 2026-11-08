#!/bin/sh
# Fails if any commit in the range lacks a Signed-off-by matching its author.
# Usage: scripts/check-dco.sh <base>..<head>   (default: origin/main..HEAD)
# Merge commits are skipped: GitHub makes them, not the contributor.
set -eu
range=${1:-origin/main..HEAD}
bad=0
for c in $(git rev-list --no-merges "$range"); do
  author=$(git log -1 --format='%an <%ae>' "$c")
  if ! git log -1 --format='%(trailers:key=Signed-off-by,valueonly)' "$c" | grep -qxF "$author"; then
    echo "missing or mismatched Signed-off-by: $(git log -1 --format='%h %s' "$c") (author: $author)"
    bad=1
  fi
done
[ "$bad" = 0 ] && echo "DCO: every commit in $range is signed off" || {
  echo "Fix with: git rebase --signoff <base>  (see CONTRIBUTING.md)"; exit 1; }
