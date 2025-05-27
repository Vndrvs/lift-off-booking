from data_init.database_initializer import engine, Flight
from booking.booking_controller import PromptForFlightId, PromptForCancelId, CollectBookingInfo, CreateBookingModel, InsertBooking, CancelBooking
from booking.validators import ValidateFlightData, ValidateBookingId
from sqlalchemy.orm import Session

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from queries.get_ticket_fare import GetTicketFare

def BookingFlow() -> float | None:
    try:
        flightId = PromptForFlightId()
        isBookable = ValidateFlightData(flightId)
        
        if isBookable:
            fName, sName, email = CollectBookingInfo()
            newBooking = CreateBookingModel(flightId, fName, sName, email)
            stmt = InsertBooking(newBooking)

            with Session(bind=engine) as session:
                fare_stmt = GetTicketFare(flightId)
                ticket_fare = session.execute(fare_stmt).scalar()
                
                session.execute(stmt)
                session.commit()

            print("Reservation successful.")
            return ticket_fare

        else:
            print("Reservation failed.")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def CancelFlow():

    try:
        bookingId = PromptForCancelId()
        isCancellable = ValidateBookingId(bookingId)

        if isCancellable:
            stmt = CancelBooking(bookingId)
            with Session(bind=engine) as session:
                session.execute(stmt)
                session.commit()
            print("Cancellation successful.")
        else:
            print("No booking exists with the given id.")

    except Exception as e:
        print(f"Error: {e}")