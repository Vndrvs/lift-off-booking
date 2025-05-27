from sqlalchemy import select
from sqlalchemy.orm import aliased
from sqlalchemy.sql import Select
from data_init.database_initializer import Flight, Airport, City, Country

def GetAllFlights() -> Select:

    # duplicate record type handling
    origin_airport = aliased(Airport)
    destination_airport = aliased(Airport)
    origin_city = aliased(City)
    destination_city = aliased(City)
    origin_country = aliased(Country)
    destination_country = aliased(Country)

    # query all flights from db
    allFlights = (
        select(Flight)
        .join(Flight.airline)
        .join(origin_airport, Flight.origin_airport)
        .join(origin_city, origin_airport.city)
        .join(origin_country, origin_city.country)
        .join(destination_airport, Flight.destination_airport)
        .join(destination_city, destination_airport.city)
        .join(destination_country, destination_city.country)
    )

    return allFlights
