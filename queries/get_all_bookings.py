from sqlalchemy import select
from sqlalchemy.sql.dml import Select
from data_init.database_initializer import Booking, Flight, Airport, City

def GetAllBookings() -> Select:

    allBookings = (
        select(Booking)
        .join(Booking.flight)
        .join(Flight.origin_airport)
        .join(Airport.city)
        .join(City.country)
    )

    return allBookings