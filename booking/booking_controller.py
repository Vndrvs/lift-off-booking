import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from booking.validators import validate_name, validate_email
#from booking.booking_logic import process_booking
from models.booking import BookingModel
from datetime import datetime

def CollectBookingInput(flight_ids: list[int]):

    while True:
        firstName = input("First name: ")
        surname = input("Surname: ")
        email = input("Email: ")
       # if not validate_email(email):
           # print("Invalid email.")
           # continue

        try:
            flightId = int(input("Enter Flight number: "))
            if flightId not in flight_ids:
                print("Invalid Flight number.")
                continue

        except ValueError:
            print("Please only type numbers.")
            continue

        break

    return BookingModel(
        bookingDate=datetime.now().isoformat(),
        flightId=flightId,
        firstName=firstName,
        surname=surname,
        email=email
    )

def InsertBooking(booking: BookingModel):

    

