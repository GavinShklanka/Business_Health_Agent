from langgraph.graph import StateGraph, END
from app.state import AgentState

from app.nodes.intent import collect_intent
from app.nodes.michael_profile import retrieve_michael_profile
from app.nodes.governance_retrieval import retrieve_governance_sources
from app.nodes.funding_retrieval import retrieve_funding_sources
from app.nodes.proposal import generate_proposal
from app.nodes.email_writer import draft_email
from app.nodes.hitl import human_approval
from app.nodes.send_email import send_email_node


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("intent", collect_intent)
    workflow.add_node("profile", retrieve_michael_profile)
    workflow.add_node("governance", retrieve_governance_sources)
    workflow.add_node("funding", retrieve_funding_sources)
    workflow.add_node("proposal", generate_proposal)
    workflow.add_node("draft", draft_email)
    workflow.add_node("hitl", human_approval)
    workflow.add_node("send", send_email_node)

    workflow.set_entry_point("intent")

    workflow.add_edge("intent", "profile")
    workflow.add_edge("profile", "governance")
    workflow.add_edge("governance", "funding")
    workflow.add_edge("funding", "proposal")
    workflow.add_edge("proposal", "draft")
    workflow.add_edge("draft", "hitl")
    workflow.add_edge("hitl", "send")
    workflow.add_edge("send", END)

    return workflow.compile()
