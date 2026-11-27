from fastapi import FastAPI

from sentinel.agents.registry import list_agents
from sentinel.config import get_settings
from sentinel.integrations.artex.adapter import ArtexAdapter
from sentinel.schemas import AgentInfo, HealthResponse, ScopeCheckRequest, ScopeCheckResponse
from sentinel.security.policy import check_target_scope

settings = get_settings()
app = FastAPI(title="SENTINEL Cyber Intelligence API", version="0.1.0", description="Phase 1 foundation. No active scanning or exploitation endpoints are exposed.")
artex_adapter = ArtexAdapter(enabled=settings.artex_enabled)


@app.get("/health", response_model=HealthResponse, tags=["operations"])
def health() -> HealthResponse:
    return HealthResponse()


@app.get("/ready", tags=["operations"])
def ready() -> dict[str, str]:
    return {"status": "ready"}


@app.get("/v1/agents", response_model=list[AgentInfo], tags=["agents"])
def agents() -> list[AgentInfo]:
    return [AgentInfo(name=a.name, purpose=a.purpose, enabled=a.enabled) for a in list_agents()]


@app.get("/v1/integrations/artex", tags=["integrations"])
def artex_status() -> dict[str, str]:
    return artex_adapter.health()


@app.post("/v1/policy/check-scope", response_model=ScopeCheckResponse, tags=["policy"])
def check_scope(request: ScopeCheckRequest) -> ScopeCheckResponse:
    decision = check_target_scope(request.hostname, settings.allowed_targets, request.authorization_reference)
    return ScopeCheckResponse(hostname=request.hostname, authorized=decision.authorized, reason=decision.reason)
