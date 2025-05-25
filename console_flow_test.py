from queries.get_all_flights import getAllFlights 
from sqlalchemy.orm import Session
from database_initializer import engine
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
    print("└" + "─" * 51 + "┘")
    
    while True:
        try:
            choice = int(input("Please enter a number to choose your next step (1 - Book a Flight, 2 - Cancel Booking, 3 - Check Booking List): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
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
            flight.airway.name[:15]
        ))

    print("└" + "─" * (totalWidth - 2) + "┘")
    input("Please enter the number of the flight you wish to book a ticket for: ")

def getFlightsInitializer():

    try:
        flightData = getAllFlights()
        flights = session.execute(flightData).scalars().all()

        if not flights:
                print("No flights are available currently.")
                input("Press Enter to return to main menu.")
                return
        
        displayFlightList(flights)
        
    except Exception as e:
        print((f"Couldn't retrieve flights: {str(e)}"))
        input("Press Enter to return to main menu.")


def inputHandler():
    while True:
        session = Session(bind=engine)
        choice = displayMainMenu()

        if choice == 1:
            getFlightsInitializer()
        elif choice == 2:
            print("Cancel Booking - Coming Soon")
            input("Press Enter to return to main menu.")
        elif choice == 3:
            print("Booking List - Coming Soon")
            input("Press Enter to return to main menu.")

inputHandler()

