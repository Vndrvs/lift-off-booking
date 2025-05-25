from abc import ABC
from datetime import datetime

class FlightBase(ABC):
    def __init__(self, id, date, airway_id, origin_airport_id, destination_airport_id, is_international):
        self.id = id
        self.airway_id = airway_id
        self.origin_airport_id = origin_airport_id
        self.destination_airport_id = destination_airport_id
        self.is_international = is_international
        self.date = self._ensure_datetime(date)