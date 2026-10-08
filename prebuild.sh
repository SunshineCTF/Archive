#!/bin/bash
# Top-level archive workspace prebuild: runs during pwnmake image init.
#
# Install docker compose v2 as a CLI plugin plus a `docker-compose` shim, so that
# PwnableHarness's compose integration (and the check macros) can build and start
# the docker-compose challenges from inside the pwnmake container -- making a
# single top-level `pwnmake` able to drive every challenge (no separate deploy
# script needed).
set -e
COMPOSE_VERSION=v2.29.7
PLUGIN_DIR=/usr/libexec/docker/cli-plugins
mkdir -p "$PLUGIN_DIR"
if [ ! -x "$PLUGIN_DIR/docker-compose" ]; then
	curl -fsSL "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64" \
		-o "$PLUGIN_DIR/docker-compose"
	chmod +x "$PLUGIN_DIR/docker-compose"
fi
# Shim so the classic `docker-compose <args>` (used by PwnableHarness) maps to v2.
cat > /usr/local/bin/docker-compose <<'SH'
#!/bin/sh
exec docker compose "$@"
SH
chmod +x /usr/local/bin/docker-compose
