
import csv
from models.airline import AirlineModel

def loadAirlinesFromCsv(path: str) -> list[AirlineModel]:

    localFlights = []
    internationalFlights = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    date = row["date"].strip()
                    isInternational = row["is_international"]
                    airlineId = row["airway_id"]
                    originAirportId = row["origin_airport_id"]
                    destinationAirportId = row["destination_airport_id"]

                    localFlights.append(AirlineModel(id, name, hqCityId))

                except (KeyError, ValueError) as e:
                    print(f"Row {i} skipped because of an error: {e}")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return airlines
