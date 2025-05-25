from flight import FlightBase

class InternationalFlightModel(FlightBase):
    def __init__(self, id, date, airlineId, originAirportId, destinationAirportId, ticketFare, passengerLimit):
        super().__init__(
            id=id,
            date=date,
            isInternational=True,
            airlineId=airlineId,
            originAirportId=originAirportId,
            destinationAirportId=destinationAirportId,
            ticketFare=ticketFare,
            passengerLimit=passengerLimit
        )