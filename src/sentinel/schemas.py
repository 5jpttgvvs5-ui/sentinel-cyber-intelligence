from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str = "sentinel-api"
    version: str = "0.1.0"


class AgentInfo(BaseModel):
    name: str
    purpose: str
    enabled: bool = False


class ScopeCheckRequest(BaseModel):
    hostname: str = Field(min_length=1, max_length=253)
    authorization_reference: str | None = Field(default=None, max_length=500)


class ScopeCheckResponse(BaseModel):
    hostname: str
    authorized: bool
    reason: str
