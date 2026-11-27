"""Non-operational ARTEX integration boundary.

Phase 1 intentionally does not import, vendor, launch, or control ARTEX. This adapter
only defines the normalized contract SENTINEL can use after a separate security,
provenance, and license review. No target testing is implemented here.
"""

from dataclasses import dataclass
from enum import StrEnum


class AdapterState(StrEnum):
    DISABLED = "disabled"
    REVIEW_REQUIRED = "review_required"


@dataclass(frozen=True)
class ArtexFinding:
    external_id: str
    title: str
    severity: str | None
    evidence_reference: str | None
    source: str = "artex"


class ArtexAdapter:
    def __init__(self, enabled: bool = False) -> None:
        self.state = AdapterState.REVIEW_REQUIRED if enabled else AdapterState.DISABLED

    def health(self) -> dict[str, str]:
        return {"integration": "artex", "state": self.state.value, "execution": "not_implemented", "note": "No ARTEX process, network client, or pentest action is available in Phase 1."}

    def import_finding(self, payload: dict[str, object]) -> ArtexFinding:
        """Normalize a finding supplied by a trusted offline export only."""
        required = ("external_id", "title")
        if any(not isinstance(payload.get(key), str) or not payload[key].strip() for key in required):
            raise ValueError("external_id and title are required strings")
        severity, evidence = payload.get("severity"), payload.get("evidence_reference")
        return ArtexFinding(str(payload["external_id"]), str(payload["title"]), severity if isinstance(severity, str) else None, evidence if isinstance(evidence, str) else None)
