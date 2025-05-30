from datetime import datetime

class BookingModel:
    def __init__(
        self,
        bookingDate: str,
        flightId: int,
        firstName: str,
        surname: str,
        email: str
    ):
        self.bookingDate: datetime = datetime.fromisoformat(bookingDate)
        self.flightId = flightId
        self.firstName = firstName
        self.surname = surname
        self.email = email