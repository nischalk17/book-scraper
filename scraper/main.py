import os
from .scraper import scrape_all_books
from .utils import save_to_json, save_to_csv


def main():
    print("Book Scraper Starting...\n")
    os.makedirs("data", exist_ok=True)

    books = scrape_all_books()
    save_to_json(books, "data/books.json")
    save_to_csv(books, "data/books.csv")

    print(f"\nComplete! {len(books)} books scraped.")


if __name__ == "__main__":
    main()