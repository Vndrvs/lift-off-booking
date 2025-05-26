# loader for the 'countries' table

import csv

def loadCountries(path: str) -> list[dict]:

    countries = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    country_id = int(row["id"])
                    name = row["country"].strip()

                    if not name:
                        raise ValueError("Country name field is empty.")

                    countries.append({
                        "id": country_id,
                        "name": name
                    })
                    
                except (KeyError, ValueError) as e:
                    print(f"Row {i}: {e} skipped because of an error.")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return countries