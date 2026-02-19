import requests
import certifi
from bs4 import BeautifulSoup


def scrape_smu_profile():
    url = "https://www.smu.ca/researchers/sobey/profiles/michael-zhang.html"

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
            "source": "SMU Website",
            "url": url,
            "content": text[:3000]
        }

    except Exception as e:
        return {
            "source": "SMU Website",
            "url": url,
            "error": str(e),
            "content": ""
        }
