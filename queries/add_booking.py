from typing import Dict, Any
from sqlalchemy import Insert, insert
from data_init.database_initializer import Booking

def InsertBooking(bookingData: Dict[str, Any]) -> Insert:

    newBooking = insert(Booking).values(bookingData)
    
    return newBooking