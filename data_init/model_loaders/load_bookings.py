# function flow:
# 1. LoadBookingsFromCsv expects a csv and examines the results
# 2. PrepareObjects creates a list of dictionaries which contains the data of the instances
# 3. (External step) run_loaders.py commits the inserts into the session

import csv
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from models.booking import BookingModel

def LoadBookingsFromCsv(path: str) -> list[BookingModel]:

    bookings = []
    
    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                try:
                    bookingDate = row["booking_date"]
                    flightId = int(row["flight_id"].strip())
                    firstName = row["first_name"]
                    surname = row["surname"]
                    email = row["email"]

                    bookings.append(BookingModel(bookingDate, flightId, firstName, surname, email))

                except (KeyError, ValueError) as e:
                    print(f"{i}. row skipped because of an error: {e}")

    except FileNotFoundError:
        print(f"File not found: {path}")

    except Exception as e:
        print(f"Error reading file: {e}")

    return bookings

def PrepareBookingList(bookings: list[BookingModel]) -> list[dict]:

    bookingList = []

    for booking in bookings:
        obj = {
            "booking_date": booking.bookingDate,
            "flight_id": booking.flightId,
            "first_name": booking.firstName,
            "surname": booking.surname,
            "email": booking.email
        }
        bookingList.append(obj)

    return bookingList