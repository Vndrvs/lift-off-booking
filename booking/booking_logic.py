from booking.booking_controller import PromptForFlightId, PromptForCancelId, CollectBookingInfo, CreateBookingModel, InsertBooking, CancelBooking
from booking.validators import ValidateFlightData, ValidateBookingId
from sqlalchemy.orm import Session
from data_init.database_initializer import engine

def BookingFlow():
    
    try:
        flightId = PromptForFlightId()
        isBookable = ValidateFlightData(flightId)
        
        if isBookable:
            fName, sName, email = CollectBookingInfo()
            newBooking = CreateBookingModel(flightId, fName, sName, email)
            stmt = InsertBooking(newBooking)  # this prepares the SQL
            
            with Session(bind=engine) as session:
                session.execute(stmt)
                session.commit()
            InsertBooking(newBooking)
            print("Reservation successful.")

        else:
            print("Reservation failed.")

    except Exception as e:
        print(f"Error: {e}")

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