from sqlalchemy import select
from sqlalchemy.sql import Select
from data_init.database_initializer import Booking

def CheckIfBookingIdExists(bookingId: int) -> Select:

    result = select(Booking.id).where(Booking.id == bookingId)

    return result