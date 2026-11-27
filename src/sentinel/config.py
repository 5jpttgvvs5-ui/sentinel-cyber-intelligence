from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    database_url: str = "postgresql+psycopg://sentinel:change-me@localhost:5432/sentinel"
    redis_url: str = "redis://localhost:6379/0"
    sentinel_allowed_targets: str = ""
    artex_enabled: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def allowed_targets(self) -> frozenset[str]:
        return frozenset(host.strip().lower().rstrip(".") for host in self.sentinel_allowed_targets.split(",") if host.strip())


@lru_cache
def get_settings() -> Settings:
    return Settings()
