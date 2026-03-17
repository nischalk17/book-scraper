import json
import pandas as pd
from datetime import date

RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3,
    "Four": 4, "Five": 5
}

def get_today():
    return str(date.today())

def save_to_json(data, filepath="data/books.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} books to {filepath}")

def save_to_csv(data, filepath="data/books.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding="utf-8")
    print(f"Saved {len(data)} books to {filepath}")