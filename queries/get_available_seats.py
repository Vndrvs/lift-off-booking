from sqlalchemy import Select, select, func
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_init.database_initializer import Flight, Booking, engine

# queries the total passenger limits and deducts the number of bookings in the table for that flight
def GetAvailableSeatCount(flightId: int) -> Select:

    stmt = (
        select(Flight.passenger_limit - func.count(Booking.id))
        .join(Booking, Booking.flight_id == Flight.id, isouter=True)
        .where(Flight.id == flightId)
        .group_by(Flight.id, Flight.passenger_limit)
    )

    return stmt