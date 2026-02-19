from app.tools.smu_scraper import scrape_smu_profile
from app.tools.scholar_scraper import scrape_scholar
from app.tools.semantic_scholar import scrape_semantic_scholar

def retrieve_michael_profile(state):
    print("\n--- Retrieving Michael Profile ---\n")

    smu_data = scrape_smu_profile()

    try:
        scholar_data = scrape_scholar()
        print("Google Scholar successful.")
    except Exception as e:
        print("Scholar failed. Using Semantic Scholar fallback.")
        scholar_data = scrape_semantic_scholar()

    state["michael_profile"] = {
        "smu": smu_data,
        "scholar": scholar_data
    }

    return state
