from sqlalchemy import Select, select
from data_init.database_initializer import Flight

def GetTicketFare(flightId: int) -> Select:

    result = select(Flight.ticket_fare).where(Flight.id == flightId)
    
    return result