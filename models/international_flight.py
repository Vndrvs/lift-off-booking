from models.flight import FlightBase

class InternationalFlightModel(FlightBase):
    def __init__(self, date, airlineId, originAirportId, destinationAirportId, ticketFare, passengerLimit):
        super().__init__(
            date=date,
            isInternational=True,
            airlineId=int(airlineId),
            originAirportId=int(originAirportId),
            destinationAirportId=int(destinationAirportId),
            ticketFare=int(ticketFare),
            passengerLimit=int(passengerLimit)
        )