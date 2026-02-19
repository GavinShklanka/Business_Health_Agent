from typing import TypedDict, Optional, Dict


class AgentState(TypedDict, total=False):
    # --- API Input ---
    user_input: str
    parameters: Dict

    # --- Intent Processing ---
    user_intent: str
    positioning_mode: str

    # --- Retrieved Data ---
    profile_data: dict
    governance_data: dict
    funding_data: dict

    # --- Generation Outputs ---
    proposal: str
    draft_email: str

    # --- Email Metadata ---
    sender_email: str
    recipient_email: str

    # --- Approval ---
    approved: bool
