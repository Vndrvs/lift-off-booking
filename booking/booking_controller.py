import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from datetime import datetime
from sqlalchemy import Insert, Delete
from models.booking import BookingModel
from queries.add_booking import InsertBooking as InsertBookingQuery
from queries.delete_booking import DeleteBooking


# prompts user for flight id (later used in validator)
def PromptForFlightId() -> int:

    flightId = int(input("Please enter the number of the flight you want to book a ticket for: "))

    return flightId

# prompts user for flight information (stored in booking instance)
def CollectBookingInfo() -> tuple[str, str, str]:

    firstName = input("First name: ")
    surname = input("Surname: ")
    email = input("Email: ")

    return firstName, surname, email

def PromptForCancelId() -> int:

    bookingId = int(input("Please enter the number of the flight you want to cancel your booking for: "))

    return bookingId

def CreateBookingModel(flightId: int, firstName: str, surname: str, email: str) -> BookingModel:

    instance = BookingModel(
        bookingDate=datetime.now().isoformat(),
        flightId=flightId,
        firstName=firstName,
        surname=surname,
        email=email
    )

    return instance

def InsertBooking(booking: BookingModel) -> Insert:
    booking_dict = {
        "booking_date": booking.bookingDate,
        "flight_id": booking.flightId,
        "first_name": booking.firstName,
        "surname": booking.surname,
        "email": booking.email
    }

    return InsertBookingQuery(booking_dict)

def CancelBooking(booking_id: int) -> Delete:

    stmt = DeleteBooking(booking_id)

    return stmt