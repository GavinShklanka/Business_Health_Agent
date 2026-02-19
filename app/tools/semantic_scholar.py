import requests
import certifi


def scrape_semantic_scholar():
    url = "https://api.semanticscholar.org/graph/v1/author/RHcPtfkAAAAJ?fields=name,papers.title,papers.year"

    try:
        response = requests.get(
            url,
            verify=certifi.where(),
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        return {
            "source": "Semantic Scholar API",
            "url": url,
            "content": data
        }

    except Exception as e:
        return {
            "source": "Semantic Scholar API",
            "url": url,
            "error": str(e),
            "content": {}
        }
