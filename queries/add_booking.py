from typing import Dict, Any
from sqlalchemy import insert
from sqlalchemy.sql.dml import Insert
from database_initializer import Booking

def InsertBooking(bookingData: Dict[str, Any]) -> Insert:

    newBooking = insert(Booking).values(bookingData)
    
    return newBooking