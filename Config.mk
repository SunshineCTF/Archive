# Top-level SunshineCTF archive workspace.
#
# Running `pwnmake` here treats all per-year repos (17..25) as ONE workspace, so
# a single non-recursive `pwnmake -jN <target>` parallelizes across every year's
# challenges at once: build, check, check-full, publish, and docker-start/-stop (both
# PwnableHarness and docker-compose challenges). Each repo also still works standalone (it
# has its own .pwnmake).
#
# Skip the Pegasus submodules: they're managed separately and their prebuild.sh
# uses pip in a way that doesn't fit the shared image init.
RECURSION_BLACKLIST += %/Pegasus

# Exclude every repo's build/publish/cache dirs (the default blacklist only covers
# the top-level ./publish). Stale per-repo publish/ dirs contain copied Build.mk
# files that would otherwise be picked up as bogus projects.
RECURSION_BLACKLIST += %/publish %/.build
