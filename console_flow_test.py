from queries.get_all_flights import get_all_flights 
from sqlalchemy.orm import Session
from database_initializer import engine
import logging

session = Session(bind=engine)

for name in logging.root.manager.loggerDict:
    if name.startswith("sqlalchemy"):
        logging.getLogger(name).setLevel(logging.CRITICAL)

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logging.getLogger('sqlalchemy.pool').setLevel(logging.WARNING)


def display_main_menu() -> int:

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

def display_flight_list(flight_list):

    column_width = "| {:<4} | {:<19} | {:<10} → {:<10} | {:<15} |"
    
    total_width = len(column_width.format("", "", "", "", ""))
    
    print("\n")
    print("┌" + "─" * (total_width - 2) + "┐")
    print("|{:^{width}}|".format("Flight List - Departures", width=total_width - 2))
    print("|" + "─" * (total_width - 2) + "|")

    for flight in flight_list:
        print(column_width.format(
            flight.id,
            flight.date.strftime("%Y-%m-%d %H:%M"),
            flight.origin_airport.code,
            flight.destination_airport.code,
            flight.airway.name[:15]
        ))

    print("└" + "─" * (total_width - 2) + "┘")
    input("Please enter the number of the flight you wish to book a ticket for: ")

def get_flights_initializer():

    try:
        flight_data = get_all_flights()
        flights = session.execute(flight_data).scalars().all()

        if not flights:
                print("NO FLIGHTS AVAILABLE")
                input("Press Enter to return to main menu...")
                return
        
        display_flight_list(flights)
        
    except Exception as e:
        print((f"ERROR RETRIEVING FLIGHTS: {str(e)}"))
        input("Press Enter to return to main menu...")


def input_handler():
    while True:
        session = Session(bind=engine)
        choice = display_main_menu()

        if choice == 1:
            get_flights_initializer()
        elif choice == 2:
            print("Cancel Booking - Coming Soon")
            input("Press Enter to return to main menu...")
        elif choice == 3:
            print("Booking List - Coming Soon")
            input("Press Enter to return to main menu...")

input_handler()

