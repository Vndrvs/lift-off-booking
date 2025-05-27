from queries.get_all_flights import GetAllFlights 
from queries.get_all_bookings import GetAllBookings
from sqlalchemy.orm import Session
from data_init.database_initializer import engine
from models.flight import FlightBase
from models.booking import BookingModel
from booking.booking_logic import BookingFlow, CancelFlow

import logging

session = Session(bind=engine)

for name in logging.root.manager.loggerDict:
    if name.startswith("sqlalchemy"):
        logging.getLogger(name).setLevel(logging.CRITICAL)

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logging.getLogger('sqlalchemy.pool').setLevel(logging.WARNING)

def displayMainMenu() -> int:

    print("\n")
    print("┌" + "─" * 51 + "┐")
    print("|{:^51}|".format("Welcome to Liftoff — Flight Booking Console"))
    print("|" + "─" * 51 + "|")
    print("|{:^51}|".format("1 - Book a Flight"))
    print("|{:^51}|".format("2 - Cancel Booking"))
    print("|{:^51}|".format("3 - Check Booking List"))
    print("|{:^51}|".format("4 - Exit"))
    print("└" + "─" * 51 + "┘")
    
    while True:
        try:
            choice = int(input("Please enter a number to choose your next step (1-2-3-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid input. Please choose 1, 2, 3 or 4.")
        except ValueError:
            print("Please enter a valid number.")

def displayFlightList(flightList):

    columnWidth = "| {:<4} | {:<19} | {:<10} → {:<10} | {:<15} |"
    
    totalWidth = len(columnWidth.format("", "", "", "", ""))
    
    print("\n")
    print("┌" + "─" * (totalWidth - 2) + "┐")
    print("|{:^{width}}|".format("Flight List - Departures", width=totalWidth - 2))
    print("|" + "─" * (totalWidth - 2) + "|")

    for flight in flightList:
        print(columnWidth.format(
            flight.id,
            flight.date.strftime("%Y-%m-%d %H:%M"),
            flight.origin_airport.code,
            flight.destination_airport.code,
            flight.airline.name[:15]
        ))

    print("└" + "─" * (totalWidth - 2) + "┘")


def getFlightsInitializer() -> list[FlightBase] | None:
    try:
        with Session(bind=engine) as session:
            flightData = GetAllFlights()
            flights = session.execute(flightData).scalars().all()

            if not flights:
                print("No flights are available currently.")
                input("Press Enter to return to main menu.")
                return None

            return flights

    except Exception as e:
        print(f"Flight retrieval error: {str(e)}")
        input("Press Enter to return to main menu.")
        return None
    
def displayBookingList(bookingList):

    columnWidth = "| {:<4} | {:<19} | {:<10} → {:<10} | {:<20} |"
    
    totalWidth = len(columnWidth.format("", "", "", "", ""))
    
    print("\n")
    print("┌" + "─" * (totalWidth - 2) + "┐")
    print("|{:^{width}}|".format("Booking List", width=totalWidth - 2))
    print("|" + "─" * (totalWidth - 2) + "|")

    for booking in bookingList:
        print(columnWidth.format(
            booking.id,
            booking.booking_date.strftime("%Y-%m-%d %H:%M"),
            booking.flight.origin_airport.code,
            booking.flight.destination_airport.code,
            f"{booking.first_name} {booking.surname}"
        ))

    print("└" + "─" * (totalWidth - 2) + "┘")

def getBookingsInitializer() -> list[BookingModel] | None:
    try:
        with Session(bind=engine) as session:
            bookingData = GetAllBookings()
            bookings = session.execute(bookingData).scalars().all()

            if not bookings:
                print("No bookings were found.")
                input("Press Enter to return to main menu.")
                return None

            return bookings

    except Exception as e:
        print(f"Booking retrieval error: {str(e)}")
        input("Press Enter to return to main menu.")
        return None

def InputHandler():
    while True:
        session = Session(bind=engine)
        choice = displayMainMenu()

        if choice == 1:
            flights = getFlightsInitializer()
            if flights:
                displayFlightList(flights)
                ticketFare = BookingFlow()
                print(f"Ticket fare: {ticketFare} HUF.")
                input("Press Enter to return to main menu.")
        elif choice == 2:
            bookings = getBookingsInitializer()
            if bookings:
                displayBookingList(bookings)
                CancelFlow()
                input("Press Enter to return to main menu.")
        elif choice == 3:
            bookings = getBookingsInitializer()
            displayBookingList(bookings)
            input("Press Enter to return to main menu.")
        elif choice == 4:
            print("Goodbye!")
            break