# added 'isInternational' variable which is used for proper database schema mapping

from flight import FlightBase

class LocalFlightModel(FlightBase):
    def __init__(self, id, date, airlineId, originAirportId, destinationAirportId):
        super().__init__(id, date, airlineId, originAirportId, destinationAirportId, isInternational=False)