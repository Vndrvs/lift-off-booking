from sqlalchemy import Select, select
from data_init.database_initializer import Flight

def CheckIfFlightIdExists(flightId: int) -> Select:

    result = select(Flight.id).where(Flight.id == flightId)

    return result