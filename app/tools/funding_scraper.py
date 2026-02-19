import requests
import certifi
from bs4 import BeautifulSoup


def scrape_nserc_ai():
    url = "https://www.nserc-crsng.gc.ca/ResearchPortal-PortailDeRecherche/"

    try:
        response = requests.get(
            url,
            verify=certifi.where(),
            timeout=10
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)

        return {
            "title": "NSERC AI & Responsible Innovation Funding",
            "url": url,
            "content": text[:2000]
        }

    except Exception as e:
        return {
            "title": "NSERC AI & Responsible Innovation Funding",
            "url": url,
            "error": str(e),
            "content": ""
        }


def scrape_responsible_ai_canada():
    url = "https://ised-isde.canada.ca/site/ised/en/responsible-ai"

    try:
        response = requests.get(
            url,
            verify=certifi.where(),
            timeout=10
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)

        return {
            "title": "Canadian Responsible AI Strategy",
            "url": url,
            "content": text[:2000]
        }

    except Exception as e:
        return {
            "title": "Canadian Responsible AI Strategy",
            "url": url,
            "error": str(e),
            "content": ""
        }
