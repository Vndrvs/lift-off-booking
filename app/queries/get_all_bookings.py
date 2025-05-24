from sqlalchemy import select
from sqlalchemy.sql.dml import Select
from database_initializer import Booking, Flight, Airport, City

def get_all_bookings() -> Select:

    all_bookings = (
        select(Booking)
        .join(Booking.flight)
        .join(Flight.origin_airport)
        .join(Airport.city)
        .join(City.country)
    )

    return all_bookings