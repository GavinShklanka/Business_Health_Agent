def draft_email(state):
    print("\n--- Drafting Email ---\n")

    email = """
Subject: PhD Inquiry – AI Governance and Enterprise Decision Systems

Dear Dr. Zhang,

I hope this message finds you well.

Following our previous discussions regarding the possibility of pursuing a PhD under your supervision, I have been refining the focus of my proposed research direction. I am increasingly drawn toward the study of AI governance and policy-constrained enterprise decision support systems, particularly within regulated and operationally complex environments.

My intention is to design and evaluate a governance-aware agentic framework capable of delivering structured, auditable decision support to enterprises across industries. The architecture would integrate controlled retrieval, policy constraints, human-in-the-loop escalation, and traceable system outputs. The objective would not be autonomous decision-making, but rather the development of a resilient orchestration layer that ensures compliance, transparency, and long-term scalability under evolving regulatory conditions.

I believe this research direction aligns naturally with your work in AI for Business and Health, particularly your emphasis on structured analytics, operational modeling, and decision-oriented systems. At the same time, it explores a forward-looking avenue for the Sobey School of Business—positioning the program at the intersection of enterprise analytics, responsible AI deployment, and applied governance frameworks.

Given the growing institutional and federal emphasis on responsible AI and enterprise risk management, this direction may also create opportunities for external funding aligned with governance and compliance innovation.

I would greatly value the opportunity to discuss this further and refine the scope under your guidance.

Sincerely,

Gavin Shklanka
Master of Business Analytics (MBAN)
Sobey School of Business
Saint Mary’s University

B.A. in Psychology & Business



"""

    # Save using correct state key (new architecture)
    state["draft_email"] = email

    # ---------- METADATA SUMMARY BLOCK ----------
    word_count = len(email.split())

    sources_used = []

    profile_data = state.get("profile_data", {})
    funding_data = state.get("funding_data")
    governance_data = state.get("governance_data")

    if profile_data.get("smu"):
        sources_used.append("SMU Website")

    if profile_data.get("scholar"):
        sources_used.append("Semantic Scholar")

    if funding_data:
        sources_used.append("NSERC")

    if governance_data:
        sources_used.append("Canadian Responsible AI")

    print("\n----------------------------------------")
    print("Email Draft Generated")
    print("----------------------------------------")
    print(f"Length: {word_count} words")
    print("Sources Used:")

    if sources_used:
        for source in sources_used:
            print(f" - {source}")
    else:
        print(" - None")

    print("----------------------------------------")

    return state
