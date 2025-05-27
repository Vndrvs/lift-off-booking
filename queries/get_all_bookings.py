from sqlalchemy import select
from sqlalchemy.orm import joinedload
from data_init.database_initializer import Booking, Flight

def GetAllBookings():
    return (
        select(Booking)
        .options(
            joinedload(Booking.flight)
            .joinedload(Flight.origin_airport),
            joinedload(Booking.flight)
            .joinedload(Flight.destination_airport)
        )
    )