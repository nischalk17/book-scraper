import time
import requests
from bs4 import BeautifulSoup
from .parser import parse_book

BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = "https://books.toscrape.com/catalogue/"


def get_soup(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "html.parser")


def get_all_book_urls():
    """Paginate through all listing pages and return every book detail URL."""
    book_urls = []
    current_url = BASE_URL

    while True:
        print(f"Scanning: {current_url}")
        soup = get_soup(current_url)

        for article in soup.select("article.product_pod"):
            relative_url = article.select_one("h3 a")["href"]

            # Remove all leading "../" segments
            clean = relative_url.replace("../", "")

            # If href already starts with "catalogue/", don't prepend it again
            if clean.startswith("catalogue/"):
                book_urls.append(BASE_URL + clean)
            else:
                book_urls.append(CATALOGUE_URL + clean)

        next_btn = soup.select_one("li.next a")
        if not next_btn:
            break

        next_href = next_btn["href"]
        if next_href.startswith("catalogue/"):
            current_url = BASE_URL + next_href
        else:
            current_url = CATALOGUE_URL + next_href

    return book_urls


def scrape_all_books():
    """Collect URLs then scrape each detail page. Returns list of book dicts."""
    book_urls = get_all_book_urls()
    print(f"\nFound {len(book_urls)} books. Scraping detail pages...\n")

    books = []
    for i, url in enumerate(book_urls, 1):
        try:
            soup = get_soup(url)
            book = parse_book(soup, url)
            books.append(book)
            print(f"[{i}/{len(book_urls)}] {book['name']}")
            time.sleep(0.3)
        except Exception as e:
            print(f"[{i}] ERROR — {url}: {e}")

    return books