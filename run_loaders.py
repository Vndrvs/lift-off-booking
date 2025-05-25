from sqlalchemy.orm import Session
from sqlalchemy import insert
from database_initializer import engine, Airline, Flight
from model_loaders.load_airlines import LoadAirlinesFromCsv, PrepareAirlineList
from model_loaders.load_flights import LoadFlightsFromCsv, PrepareFlightList
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

def LoadAllData():
    airlines = LoadAirlinesFromCsv("data/airlines.csv")
    airlineRows = PrepareAirlineList(airlines)

    flights = LoadFlightsFromCsv("data/flights.csv")
    flightRows = PrepareFlightList(flights)

    try:
        with Session(bind=engine) as session:
            if airlineRows:
                stmt = sqlite_insert(Airline).values(airlineRows)
                stmt = stmt.on_conflict_do_nothing(index_elements=["name"])
                session.execute(stmt)
                print(f"{len(airlineRows)} airlines inserted.")

            if flightRows:
                session.execute(insert(Flight), flightRows)
                print(f"{len(flightRows)} flights inserted.")

            session.commit()

    except Exception as e:
        print(f"Insertion failed: {e}")

LoadAllData()