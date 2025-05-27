from sqlalchemy import Delete, delete
from data_init.database_initializer import Booking

def DeleteBooking(booking_id: int) -> Delete:

    deletedBooking = delete(Booking).where(Booking.id == booking_id)

    return deletedBooking