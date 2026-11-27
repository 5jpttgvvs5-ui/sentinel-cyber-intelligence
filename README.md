# SENTINEL Cyber Intelligence

A cloud-first, multi-agent cyber-intelligence platform scaffold.

**Phase 1 status:** foundation scaffold only. It includes a FastAPI service, health/readiness endpoints, agent registry, a fail-closed scope policy, PostgreSQL/Redis services, and CI tests.

## Safety boundary

SENTINEL is designed for public-source security intelligence and explicitly authorized defensive testing. It does not perform scanning, exploitation, credential collection, stealth, access-control bypass, or autonomous actions against third-party systems.

The ARTEX integration in this repository is an **inert adapter contract** only. It does not vendor, launch, or execute ARTEX. A future integration must be separately reviewed for source provenance, AGPL-3.0 obligations, dependency/security posture, network isolation, target-scope enforcement, and human approval gates before any operational use.

## Stack

- Python 3.12
- FastAPI + Pydantic Settings
- PostgreSQL 16
- Redis 7
- Docker Compose
- pytest + Ruff
- ARTEX adapter interface (disabled by default; no execution capability)

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

API: http://localhost:8000  
OpenAPI: http://localhost:8000/docs  
Health: http://localhost:8000/health  
Readiness: http://localhost:8000/ready

For local development:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn sentinel.main:app --reload
pytest
ruff check .
```

## Configuration

All secrets are supplied through environment variables. Never commit `.env`, API keys, database passwords, tokens, or production credentials.

`SENTINEL_ALLOWED_TARGETS` is a comma-separated list of exact hostnames approved for a specific authorized lab deployment. Empty means no targets are authorized. The policy is deliberately fail-closed.

## Phase 1 components

- `sentinel.main`: API entry point
- `sentinel.agents.registry`: explicit registry of available agents
- `sentinel.security.policy`: fail-closed target authorization checks
- `sentinel.integrations.artex.adapter`: inert integration boundary
- `tests/`: policy and API tests

## Next phases

1. Persistent database models and migrations.
2. Public-source collectors (NVD, CISA KEV, GitHub advisories) with rate limits and provenance.
3. Evidence normalization, deduplication, and confidence scoring.
4. Durable workflow orchestration and agent memory.
5. Reviewed, isolated integrations for authorized lab testing only.

## License

No project license has been selected yet. Do not redistribute this scaffold as open source until the project owner chooses a license and reviews third-party license obligations.
