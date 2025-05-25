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
                    hqCityId = int(row["hq_city"])

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