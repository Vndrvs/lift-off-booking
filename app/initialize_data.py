from sqlalchemy import insert
from sqlalchemy.orm import Session
from database_initializer import Country, City, Airport, engine
from seeders.country_seeder import load_countries
from seeders.city_seeder import load_cities
from seeders.airport_seeder import load_airports

def seed_countries(session):

    countries = load_countries("app/data/countries.csv")
    if not countries:
        print("0 countries found.")
        return
    try:
        session.execute(insert(Country), countries)
        session.commit()
        print(f"{len(countries)} countries inserted.")
    except Exception as e:
        session.rollback()
        print(f"Insertion error: {e}")

def seed_cities(session):

    cities = load_cities("app/data/cities.csv")
    if not cities:
        print("0 cities found.")
        return

    try:
        session.execute(insert(City), cities)
        session.commit()
        print(f"{len(cities)} cities inserted.")
    except Exception as e:
        session.rollback()
        print(f"Insertion error: {e}")

def seed_airports(session):

    airports = load_airports("app/data/airports.csv")
    if not airports:
        print("0 cities found.")
        return

    try:
        session.execute(insert(Airport), airports)
        session.commit()
        print(f"{len(airports)} airports inserted.")
    except Exception as e:
        session.rollback()
        print(f"Insertion error: {e}")


def run_seeding():
    with Session(bind=engine) as session:
        #seed_countries(session)
        #seed_cities(session)
        seed_airports(session)

run_seeding()