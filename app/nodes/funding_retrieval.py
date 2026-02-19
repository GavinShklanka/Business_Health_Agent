from app.tools.funding_scraper import scrape_nserc_ai, scrape_responsible_ai_canada

def retrieve_funding_sources(state):
    print("\n--- Retrieving Funding Sources ---\n")

    raw_sources = [
        scrape_nserc_ai(),
        scrape_responsible_ai_canada(),
        {"title": "AI Gaming Market Trends", "url": "https://example.com/gaming"}
    ]

    filtered = []

    for s in raw_sources:
        if "AI" in s["title"] or "Responsible" in s["title"]:
            filtered.append(s)

    state["funding_sources"] = filtered

    print("Filtered Funding Sources:", filtered)

    return state
