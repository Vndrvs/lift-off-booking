import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from datetime import datetime, timezone
from sqlalchemy.orm import Session
from data_init.database_initializer import engine
from queries.get_flight_time import GetFlightTime
from queries.get_available_seats import GetAvailableSeatCount
from queries.select_flight_id import CheckIfIdExists

def ValidateAvailableSeats(flightId: int) -> bool:

    stmt = GetAvailableSeatCount(flightId)

    with Session(bind=engine) as session:
        result = session.execute(stmt).scalar()

        if result is None or result == 0:
            return False
        else:
            return True

def ValidateFlightId(flightId: int) -> bool:

    stmt = CheckIfIdExists(flightId)

    with Session(bind=engine) as session:
        result = session.execute(stmt).scalar()

        if result is None:
            return False
        else:
            return True

def ValidateBookingTime(flightId: int) -> bool:

    now = datetime.now(timezone.utc)
    stmt = GetFlightTime(flightId)

    with Session(bind=engine) as session:
        result = session.execute(stmt).scalar()

        if result is None or (result.tzinfo is None and result.replace(tzinfo=timezone.utc) <= now) or (result.tzinfo is not None and result <= now):
            return False
        else:
            return True

# will add in later patch
def ValidateEmail():
    return 1