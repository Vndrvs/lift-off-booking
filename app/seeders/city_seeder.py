# loader for the 'cities' table

import csv

def load_cities(path: str) -> list[dict]:

    cities = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    city_id = int(row["id"])
                    name = row["name"].strip()
                    country_id = int(row["country_id"])

                    if not name:
                        raise ValueError("City name field is empty.")

                    cities.append({
                        "id": city_id,
                        "name": name,
                        "country_id": country_id
                    })
                    
                except (KeyError, ValueError) as e:
                    print(f"Row {i}: {e} skipped because of an error.")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return cities