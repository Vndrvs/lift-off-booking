import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import csv
from models.airline import AirlineModel

def loadAirlines(path: str) -> list[AirlineModel]:

    airlines = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    id = int(row["id"])
                    name = row["name"].strip()
                    hqCityId = int(row["city_id"])

                    airlines.append(AirlineModel(id, name, hqCityId))

                except (KeyError, ValueError) as e:
                    print(f"Row {i} skipped because of an error: {e}")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return airlines

def CreateModelDictionary(path: str) -> dict[int, AirlineModel]:

    airlines = loadAirlines(path)
    airlineDictionary = {}

    for airline in airlines:
        airlineDictionary[airline.id] = airline

    return airlineDictionary

if __name__ == "__main__":
    path = "data/airlines.csv"

    airlines_by_id = CreateModelDictionary(path)

    print(f"✅ Loaded {len(airlines_by_id)} airlines.\n")

    for id, airline in airlines_by_id.items():
        print(f"🛩️  ID: {id} | Name: {airline.name} | HQ City ID: {airline.hqCityId}")