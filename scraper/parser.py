from .utils import RATING_MAP, get_today

def parse_book(soup, url):
    """Extract all required fields from a book detail page soup."""

    # Name
    name = soup.select_one("h1").text.strip()

    # Rating
    rating_word = soup.select_one("p.star-rating")["class"][1]
    rating = RATING_MAP.get(rating_word, 0)

    # Description
    desc_elem = soup.select_one("#product_description + p")
    description = desc_elem.text.strip() if desc_elem else "No description available."

    # Product info table
    table_data = {
        row.select_one("th").text.strip(): row.select_one("td").text.strip()
        for row in soup.select("table.table tr")
    }

    return {
        "name": name,
        "url": url,
        "scrape_date": get_today(),
        "description": description,
        "price": table_data.get("Price (excl. tax)", "N/A"),
        "tax": table_data.get("Tax", "N/A"),
        "availability": table_data.get("Availability", "N/A"),
        "upc": table_data.get("UPC", "N/A"),
        "rating": rating,
    }