from typing import Dict, Any
from sqlalchemy import insert
from sqlalchemy.sql.dml import Insert
from database_initializer import Booking

def insertBooking(booking_data: Dict[str, Any]) -> Insert:

    new_booking = insert(Booking).values(booking_data)
    
    return new_booking