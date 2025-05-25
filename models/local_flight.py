from models.flight import FlightBase

class LocalFlightModel(FlightBase):
    def __init__(self, date, airlineId, originAirportId, destinationAirportId, ticketFare, passengerLimit):
        super().__init__(
            date=date,
            isInternational=False,
            airlineId=int(airlineId),
            originAirportId=int(originAirportId),
            destinationAirportId=int(destinationAirportId),
            ticketFare=int(ticketFare),
            passengerLimit=int(passengerLimit)
        )