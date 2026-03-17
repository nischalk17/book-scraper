# Book Scraper

A Python web scraper for [books.toscrape.com](https://books.toscrape.com/) that extracts detailed information from all 1000 books across 50 pages.

## Features

- Automatically paginates through all pages (no hardcoded page numbers)
- Visits each book's detail page individually
- Extracts structured data for every book
- Saves output as both JSON and CSV

## Extracted Fields

| Field | Description |
|---|---|
| `name` | Book title |
| `url` | Absolute URL of the book detail page |
| `scrape_date` | Date the scraper was run |
| `description` | Product description |
| `price` | Price excluding tax |
| `tax` | Tax amount |
| `availability` | Stock availability text |
| `upc` | Universal Product Code |
| `rating` | Numeric rating (1–5) |

## Project Structure
```
book-scraper/
│
├── scraper/
│   ├── __init__.py
│   ├── main.py        # Entry point — orchestrates the scrape
│   ├── scraper.py     # HTTP requests and pagination
│   ├── parser.py      # HTML parsing and field extraction
│   └── utils.py       # Shared helpers (rating map, JSON and CSV export, date)
│
├── data/
│   └── books.json     # Output file (auto-generated on run)
    └── books.csv     # Output file (auto-generated on run)
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10+
- pip

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/nischalk17/book-scraper.git
cd book-scraper
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

Run the scraper from the project root directory:
```bash
python -m scraper.main
```

Output will be saved to `data/books.json` and `data/books.csv`.

## Example Output
```json
{
  "name": "A Light in the Attic",
  "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
  "scrape_date": "2026-03-17",
  "description": "It's hard to imagine a world without A Light in the Attic...",
  "price": "£51.77",
  "tax": "£0.00",
  "availability": "In stock (22 available)",
  "upc": "a897fe39b1053632",
  "rating": 3
}
```

## Libraries Used

| Library | Purpose |
|---|---|
| `requests` | Fetching web pages |
| `beautifulsoup4` | Parsing HTML |
| `pandas` | Exporting data to CSV |

## Notes

- A 0.3 second delay is added between requests to avoid overloading the server
- Books with scrape errors are logged and skipped without crashing the run
- The `data/` folder is created automatically if it doesn't exist
- All 1000 Books across 50 pages were scrapped with correct details
```
