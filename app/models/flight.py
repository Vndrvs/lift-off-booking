from abc import ABC
from datetime import datetime

from abc import ABC
from datetime import datetime

class FlightBase(ABC):
    def __init__(
        self,
        id: int,
        date: str,
        airlineId: int,
        originAirportId: int,
        destinationAirportId: int,
        isInternational: bool
    ):
        self.id: int = id
        self.date: datetime = datetime.fromisoformat(date)
        self.isInternational: bool = isInternational
        self.airlineId: int = airlineId
        self.originAirportId: int = originAirportId
        self.destinationAirportId: int = destinationAirportId