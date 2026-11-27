from dataclasses import dataclass


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    purpose: str
    enabled: bool = False


AGENTS = (
    AgentDefinition("discovery", "Discover public, permitted security-information sources."),
    AgentDefinition("research", "Analyze collected reports and preserve source provenance."),
    AgentDefinition("threat_intel", "Normalize public threat indicators and relationships."),
    AgentDefinition("vulnerability_intel", "Correlate published vulnerability advisories."),
    AgentDefinition("community", "Use only community APIs and interactions explicitly permitted by moderators."),
    AgentDefinition("verification", "Check evidence quality, timestamps, and duplicate findings."),
)


def list_agents() -> list[AgentDefinition]:
    return list(AGENTS)
