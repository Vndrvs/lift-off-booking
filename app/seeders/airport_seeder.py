# loader for the 'airports' table

import csv

def loadAirports(path: str) -> list[dict]:

    airports = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    airport_id = int(row["id"])
                    name = row["name"].strip()
                    code = row["code"].strip()
                    city_id = int(row["city_id"])

                    if not name:
                        raise ValueError("Airport name field is empty.")

                    airports.append({
                        "id": airport_id,
                        "name": name,
                        "code": code,
                        "city_id": city_id
                    })
                    
                except (KeyError, ValueError) as e:
                    print(f"Row {i} skipped because of an error: {e}")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return airports