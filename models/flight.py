# added 'isInternational' variable which is used for proper database schema mapping

from abc import ABC
from datetime import datetime

class FlightBase(ABC):
    def __init__(
        self,
        date: str,
        isInternational: bool,
        airlineId: int,
        originAirportId: int,
        destinationAirportId: int,
        ticketFare: int,
        passengerLimit: int
    ):
        self.date: datetime = datetime.fromisoformat(date)
        self.isInternational: bool = isInternational
        self.airlineId: int = airlineId
        self.originAirportId: int = originAirportId
        self.destinationAirportId: int = destinationAirportId
        self.ticketFare: int = ticketFare
        self.passengerLimit: int = passengerLimit