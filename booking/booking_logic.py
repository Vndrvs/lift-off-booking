from booking_controller import PromptForFlightId, CollectBookingInfo, CreateBookingModel, InsertBooking
from validators import ValidateFlightData
from sqlalchemy.orm import Session
from data_init.database_initializer import engine

def FunctionFlow():
    
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

FunctionFlow()