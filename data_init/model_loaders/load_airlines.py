# function flow:
# 1. LoadAirlinesFromCsv expects a csv and returns a list of Airline objects
# 2. PrepareObjects creates a list of dictionaries which contains the data of the instances
# 3. (External step) run_loaders.py commits the inserts into the session

import csv

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from models.airline import AirlineModel


def LoadAirlinesFromCsv(path: str) -> list[AirlineModel]:

    airlines = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    id = int(row["id"])
                    name = row["name"].strip()
                    hqCityId = int(row["hq_city"])

                    airlines.append(AirlineModel(id, name, hqCityId))

                except (KeyError, ValueError) as e:
                    print(f"Row {i} skipped because of an error: {e}")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return airlines

def PrepareAirlineList(airlines: list[AirlineModel]) -> list[dict]:

    airlineList = []

    for airline in airlines:
        obj = {
            "id": airline.id,
            "name": airline.name,
            "city_id": airline.hqCityId
        }
        airlineList.append(obj)

    return airlineList