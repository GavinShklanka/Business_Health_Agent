from app.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

def generate_proposal(state):
    print("\n--- Generating Proposal Outline (LLM) ---\n")

    llm = get_llm()

    michael_data = state.get("michael_profile", {})
    governance_data = state.get("governance_sources", [])
    funding_data = state.get("funding_sources", [])
    intent = state.get("user_intent", "")

    system_prompt = """
    You are a research strategy assistant.
    Write in a professional academic tone.
    Focus on AI governance, enterprise compliance,
    policy-constrained decision systems,
    and Canadian funding alignment.
    """

    human_prompt = f"""
    User Intent:
    {intent}

    Michael Research Context:
    {michael_data}

    Governance Sources:
    {governance_data}

    Funding Sources:
    {funding_data}

    Generate:
    1. Concise research proposal summary (max 400 words)
    2. Funding alignment paragraph
    3. Governance significance paragraph
    """

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ])

    state["proposal_outline"] = response.content

    print(response.content)

    return state
