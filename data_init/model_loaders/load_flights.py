# function flow:
# 1. LoadFlightsFromCsv expects a csv and examines the results
# 2. Flights are sorted into international and local objects depending on the value of the is_international field
# 3. PrepareObjects creates a list of dictionaries which contains the data of the instances
# 4. (External step) run_loaders.py commits the inserts into the session

import csv

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from models.international_flight import InternationalFlightModel
from models.local_flight import LocalFlightModel

def LoadFlightsFromCsv(path: str) -> list:
    flights = []

    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    raw_date = row["date"].strip()
                    parts = raw_date.split(" ")
                    if len(parts) == 2 and len(parts[1].split(":")[0]) == 1:
                        parts[1] = f"0{parts[1]}"
                    date = " ".join(parts)
                    isInternational = row["is_international"].strip().lower() in ("true", "1")
                    airlineId = row["airway_id"]
                    originAirportId = row["origin_airport_id"]
                    destinationAirportId = row["destination_airport_id"]
                    ticketFare = row["ticket_fare"]
                    passengerLimit = row["passenger_limit"]

                    if not isInternational:
                        flights.append(LocalFlightModel(date, airlineId, originAirportId, destinationAirportId, ticketFare, passengerLimit))
                    else:
                        flights.append(InternationalFlightModel(date, airlineId, originAirportId, destinationAirportId, ticketFare, passengerLimit))

                except (KeyError, ValueError) as e:
                    print(f"{i}. row skipped because of error: {e}")

    except FileNotFoundError:
        print(f"File not found.")
    except Exception as e:
        print(f"Error: {e}")

    return flights

def PrepareFlightList(flights: list) -> list[dict]:
    flightList = []

    for flight in flights:
        obj = {
            "date": flight.date,
            "is_international": flight.isInternational,
            "airline_id": flight.airlineId,
            "origin_airport_id": flight.originAirportId,
            "destination_airport_id": flight.destinationAirportId,
            "ticket_fare": flight.ticketFare,
            "passenger_limit": flight.passengerLimit
        }
        flightList.append(obj)

    return flightList

