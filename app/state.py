from typing import TypedDict, Optional


class AgentState(TypedDict, total=False):
    intent: str

    profile_data: dict
    governance_data: dict
    funding_data: dict

    proposal: str
    draft_email: str

    sender_email: str
    recipient_email: str

    approved: bool
