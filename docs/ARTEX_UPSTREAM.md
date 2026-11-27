# ARTEX Community Continuation — upstream record

**Selected upstream:** [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)  
**License:** AGPL-3.0  
**Language:** Go (with a Next.js web UI)  
**Checked:** 2026-11-27  
**Observed release:** `v0.7.0`  
**Pinned main commit at review:** `e5c7bfcbdd893db26c08f0b004e0169b4ab6ca85`

## Repository selection

The original `Autumn-27/ARTEX` repository is no longer the public active source. The BaaRai repository explicitly describes itself as the actively maintained community continuation of that project. Its current architecture describes a multi-agent autonomous penetration-testing platform with a Go backend, Next.js UI, PostgreSQL, planner/worker agents, traffic recording, and an approval/guard layer.

Other public copies exist. For example, `AG-Sec/artex` is a fork of `BaaRai/ARTEX`, while `taype/ARTEX` describes itself as a derivative based on an earlier upstream commit and is rebranded as ScopeWeaver. For SENTINEL's upstream tracking, BaaRai/ARTEX is the selected canonical community continuation at the time of this review.

## Integration status in SENTINEL

The current SENTINEL adapter remains an interface/normalization boundary. The ARTEX source tree has **not** been copied into this repository, and no ARTEX executable, worker, scanner, proxy, or autonomous task runner is enabled by SENTINEL.

Reason: ARTEX is not merely a passive intelligence library; its documented planner/worker system can invoke real security tools and perform autonomous penetration testing. A wholesale source import would make those operational capabilities part of this codebase before the integration boundary, dependency graph, build process, and operational behavior have been reviewed.

## License and attribution

ARTEX declares AGPL-3.0. Before copying or modifying its source into SENTINEL, review the complete license and notices, preserve upstream copyright and attribution, track modified files, and decide how SENTINEL will comply with AGPL-3.0 obligations for distribution and network use. This note is not legal advice.

## Upstream links

- Repository: https://github.com/BaaRai/ARTEX
- Release v0.7.0: https://github.com/BaaRai/ARTEX/releases/tag/v0.7.0
- License: https://github.com/BaaRai/ARTEX/blob/main/LICENSE
- Architecture documentation: https://github.com/BaaRai/ARTEX/blob/main/docs/ARCHITECTURE.md
- Operations documentation: https://github.com/BaaRai/ARTEX/blob/main/docs/OPS.md

## Next engineering steps

1. Review and pin the exact upstream commit and release.
2. Generate a third-party component inventory and compare its dependencies against SENTINEL.
3. Define a narrow integration contract for importing structured findings and evidence metadata.
4. Keep the upstream runtime independently deployable; do not merge its worker/tool execution engine into SENTINEL's API process.
5. Add integration tests using synthetic findings and offline fixtures before considering any operational bridge.
