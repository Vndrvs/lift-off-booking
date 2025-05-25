from sqlalchemy.orm import Session
from sqlalchemy import insert
from database_initializer import engine, Airline
from model_loaders.load_airlines import loadAirlinesFromCsv, PrepareObjects

def LoadAirlines():
    airlines = loadAirlinesFromCsv("data/airlines.csv")
    rows = PrepareObjects(airlines)

    if not rows:
        print("No airlines to insert.")
        return

    try:
        with Session(bind=engine) as session:
            session.execute(insert(Airline), rows)
            session.commit()
            print(f"{len(rows)} airlines inserted.")
    except Exception as e:
        print(f"Insertion failed: {e}")

LoadAirlines()