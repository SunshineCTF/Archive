#!/bin/bash
# Delete EVERY challenge from the CTFd at $CTFCLI_URL (a local test instance).
# Refuses non-localhost URLs unless run with --force.
# CTFd 3.8 won't delete a solution that still has uploaded images, or a challenge
# that still has a solution, so remove those first (in that order).
set -e
case "$CTFCLI_URL" in
  http://127.0.0.1:*|http://localhost:*|http://127.0.0.1|http://localhost) ;;
  *) [ "$1" = "--force" ] || { echo "Refusing to wipe non-local CTFd '$CTFCLI_URL' (pass --force)" >&2; exit 1; } ;;
esac
H=(-H "Authorization: Token $CTFCLI_ACCESS_TOKEN" -H 'Content-Type: application/json')
ids() { curl -s "${H[@]}" "$CTFCLI_URL$1" | python3 -c "import json,sys;print(' '.join(str(x['id']) for x in json.load(sys.stdin)['data']))"; }
for id in $(ids "/api/v1/files?type=solution"); do curl -s -o /dev/null -X DELETE "${H[@]}" "$CTFCLI_URL/api/v1/files/$id"; done
for id in $(ids "/api/v1/solutions"); do curl -s -o /dev/null -X DELETE "${H[@]}" "$CTFCLI_URL/api/v1/solutions/$id"; done
for id in $(ids "/api/v1/challenges?view=admin"); do curl -s -o /dev/null -X DELETE "${H[@]}" "$CTFCLI_URL/api/v1/challenges/$id"; done
echo "remaining challenges: $(ids "/api/v1/challenges?view=admin" | wc -w)"
