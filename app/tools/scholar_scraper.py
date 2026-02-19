from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_scholar():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://scholar.google.com/citations?user=RHcPtfkAAAAJ")

    content = driver.page_source

    driver.quit()

    return {
        "source": "Google Scholar",
        "content": content[:3000]
    }
