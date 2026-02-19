def retrieve_governance_sources(state):
    print("\n--- Retrieving Governance Sources ---\n")

    sample_sources = [
        {"title": "Enterprise AI Governance Framework 2025", "url": "https://example.com/gov"},
        {"title": "AI Art Trends", "url": "https://example.com/art"},
        {"title": "Canadian Responsible AI Strategy", "url": "https://example.com/canada"}
    ]

    included = []
    excluded = []

    for s in sample_sources:
        if "art" in s["title"].lower():
            excluded.append(s)
        else:
            included.append(s)

    state["governance_sources"] = included

    print("Included Governance:", included)
    print("Excluded Governance:", excluded)

    return state
