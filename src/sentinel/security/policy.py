from dataclasses import dataclass
import ipaddress
import re

_HOST_RE = re.compile(r"^(?=.{1,253}$)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")


@dataclass(frozen=True)
class ScopeDecision:
    authorized: bool
    reason: str


def normalize_hostname(value: str) -> str:
    host = value.strip().lower().rstrip(".")
    if not host or "://" in host or "/" in host or ":" in host or "@" in host:
        raise ValueError("Provide a hostname only; URLs, ports and credentials are not accepted.")
    try:
        ipaddress.ip_address(host)
    except ValueError:
        pass
    else:
        raise ValueError("IP literals are not accepted by this hostname-only Phase 1 policy.")
    if not _HOST_RE.fullmatch(host):
        raise ValueError("Invalid hostname.")
    return host


def check_target_scope(hostname: str, allowed_targets: frozenset[str], authorization_reference: str | None = None) -> ScopeDecision:
    try:
        host = normalize_hostname(hostname)
    except ValueError as exc:
        return ScopeDecision(False, str(exc))
    normalized = {item.strip().lower().rstrip(".") for item in allowed_targets}
    if host not in normalized:
        return ScopeDecision(False, "Host is not on the exact allowlist.")
    if not authorization_reference or not authorization_reference.strip():
        return ScopeDecision(False, "A recorded authorization reference is required.")
    return ScopeDecision(True, "Exact allowlist match and authorization reference supplied.")
