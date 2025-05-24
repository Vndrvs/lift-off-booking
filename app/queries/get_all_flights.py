from sqlalchemy import select
from sqlalchemy.orm import aliased
from sqlalchemy.sql import Select
from database_initializer import Flight, Airport, City, Country

def get_all_flights() -> Select:

    origin_airport = aliased(Airport)
    destination_airport = aliased(Airport)
    origin_city = aliased(City)
    destination_city = aliased(City)
    origin_country = aliased(Country)
    destination_country = aliased(Country)


    all_flights = (
        select(Flight)
        .join(Flight.airway)
        .join(origin_airport, Flight.origin_airport)
        .join(origin_city, origin_airport.city)
        .join(origin_country, origin_city.country)
        .join(destination_airport, Flight.destination_airport)
        .join(destination_city, destination_airport.city)
        .join(destination_country, destination_city.country)
    )

    return all_flights
