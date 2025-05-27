from sqlalchemy import select
from sqlalchemy.sql import Select
from data_init.database_initializer import Flight

def CheckIfFlightIdExists(flightId: int) -> Select:

    result = select(Flight.id).where(Flight.id == flightId)

    return result