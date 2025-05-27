from sqlalchemy import Select, select
from data_init.database_initializer import Flight

def GetFlightTime(flightId: int) -> Select:

    result = select(Flight.date).where(Flight.id == flightId)

    return result