from sqlalchemy import select
from sqlalchemy.sql import Select
from data_init.database_initializer import Flight

def GetFlightTime(flightId: int) -> Select:

    result = select(Flight.date).where(Flight.id == flightId)

    return result