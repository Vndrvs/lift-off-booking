from sqlalchemy import delete
from sqlalchemy.sql.dml import Delete
from database_initializer import Booking

def deleteBooking(booking_id: int) -> Delete:

    deleted_booking = delete(Booking).where(Booking.id == booking_id)

    return deleted_booking