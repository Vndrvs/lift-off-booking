# component responsible for running the loader functions on the csv files
# which contain the flight and airline records which we need to instantiate
# it looks ugly and overcomplicated, but it serves a purpose:

from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from data_init.database_initializer import engine, Airline, Flight
from data_init.model_loaders.load_airlines import LoadAirlinesFromCsv, PrepareAirlineList
from data_init.model_loaders.load_flights import LoadFlightsFromCsv, PrepareFlightList
from utils.insert_logger import Logger

# inserts airlines into the table
def InsertAirlines(session):

    initializedRecords = 0

    try:
        airlines = LoadAirlinesFromCsv("data/airlines.csv")
        airline_rows = PrepareAirlineList(airlines)

        if not airline_rows:
            print("No airlines found.")
            return

        stmt = sqlite_insert(Airline).values(airline_rows)
    
        # if the airline name matches an existing one in the database, that record will be skipped
        stmt = stmt.on_conflict_do_nothing(index_elements=["name"])
        result = session.execute(stmt)
        initializedRecords = result.rowcount

        Logger(initializedRecords, "Airlines")

    except Exception as e:
        session.rollback()
        print(f"Airlines: Insertion error")

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

# inserts flights into the table
# (in real-life scenarios, the uniqueness of the flight records is not validated on the booking system side
# usually, that process is handled by the planning software of the airlines, so I had to create a makeshift solution:)
def InsertFlights(session):

    initializedRecords = 0
    try:
        flights = LoadFlightsFromCsv("data/flights.csv")
        flightRows = PrepareFlightList(flights)

        if not flightRows:
            print("No flights found.")
            return

        # loads all existing flight records already in the dbase
        existing = GetExistingFlightTuples(session)
        newRows = []

        for row in flightRows:
            flight_tuple = (
                row["date"],
                row["is_international"],
                row["airline_id"],
                row["origin_airport_id"],
                row["destination_airport_id"],
                row["ticket_fare"],
                row["passenger_limit"]
            )
            if flight_tuple not in existing:
                newRows.append(row)

        if newRows:
            session.execute(insert(Flight), newRows)
            initializedRecords = len(newRows)

        Logger(initializedRecords, "Flights")

    except Exception as e:
        session.rollback()
        print(f"Flights: Insertion error")

def LoadAllData():

    try:
        with Session(bind=engine) as session:
            InsertAirlines(session)
            InsertFlights(session)
            session.commit()
        
        print()

    except Exception as e:
        print(f"Session commit error.")