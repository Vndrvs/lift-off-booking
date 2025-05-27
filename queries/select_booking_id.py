from sqlalchemy import Select, select
from data_init.database_initializer import Booking

def CheckIfBookingIdExists(bookingId: int) -> Select:

    result = select(Booking.id).where(Booking.id == bookingId)

    return result