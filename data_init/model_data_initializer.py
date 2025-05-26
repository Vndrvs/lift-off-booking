# component responsible for running the loader functions on the csv files
# which contain records which we need to class-ify (haha)
# it looks ugly and overcomplicated, because it is ugly and overcomplicated

from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from data_init.database_initializer import engine, Airline, Flight
from data_init.model_loaders.load_airlines import LoadAirlinesFromCsv, PrepareAirlineList
from data_init.model_loaders.load_flights import LoadFlightsFromCsv, PrepareFlightList

# this tuple is responsible for loading the flight records in the database into the memory for comparison
def GetExistingFlightTuples(session):
    stmt = select(
        Flight.date,
        Flight.is_international,
        Flight.airline_id,
        Flight.origin_airport_id,
        Flight.destination_airport_id,
        Flight.ticket_fare,
        Flight.passenger_limit
    )
    result = session.execute(stmt)
    return set(result.all())

# inserts airlines into the table
def InsertAirlines(session):
    airlines = LoadAirlinesFromCsv("data/airlines.csv")
    airline_rows = PrepareAirlineList(airlines)

    if not airline_rows:
        print("No airlines found.")
        return

    stmt = sqlite_insert(Airline).values(airline_rows)
    # if the airline name matches an existing one in the database, that record will be skipped
    stmt = stmt.on_conflict_do_nothing(index_elements=["name"])
    result = session.execute(stmt)
    count = result.rowcount or 0

    if count:
        print(f"{count} airlines inserted.")
    else:
        print("No new airlines to insert.")

# inserts flights into the table
def InsertFlights(session):
    flights = LoadFlightsFromCsv("data/flights.csv")
    flight_rows = PrepareFlightList(flights)

    if not flight_rows:
        print("No flights found.")
        return

    # loads existing flight records
    existing = GetExistingFlightTuples(session)
    new_rows = []

    for row in flight_rows:
        flight_tuple = (
            row["date"],
            row["is_international"],
            row["airline_id"],
            row["origin_airport_id"],
            row["destination_airport_id"],
            row["ticket_fare"],
            row["passenger_limit"]
        )
        # if a record with 100% matching data exists in the database, it skips it
        if flight_tuple not in existing:
            new_rows.append(row)

    if new_rows:
        session.execute(insert(Flight), new_rows)
        print(f"{len(new_rows)} flights inserted.")
    else:
        print("No new flights to insert.")

def LoadAllData():
    try:
        with Session(bind=engine) as session:
            InsertAirlines(session)
            InsertFlights(session)
            session.commit()
    except Exception as e:
        print(f"Insertion error: {e}")