# this module is responsible for populating the database with base and / or testing data
# hence the name, seeder

from sqlalchemy.orm import Session
from data_init.seeders.country_seeder import loadCountries
from data_init.seeders.city_seeder import loadCities
from data_init.seeders.airport_seeder import loadAirports
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from data_init.database_initializer import Country, City, Airport, engine

# generic function for loading records from csv files
# params: 1. session 2. model (class) 3. loader function type 4. filepath 5. name of class
def SeedData(session, model, loader, path, label):

    records = loader(path)

    if not records:
        print(f"0 {label.lower()} found.")
        return

    try:
        # if the loader encounters records with name fields that already exist in the dbase, it skips them
        stmt = sqlite_insert(model).values(records).on_conflict_do_nothing(index_elements=["name"])
        result = session.execute(stmt)
        session.commit()
        
        inserted_count = result.rowcount or 0
        if inserted_count > 0:
            print(f"{inserted_count} {label.lower()} inserted.")
        else:
            print(f"No new {label.lower()} inserted.")

    except Exception as e:
        session.rollback()
        print(f"Insertion error for {label.lower()}: {e}")

# initializing the component for non-class record types
def RunSeeding():
    with Session(bind=engine) as session:
        SeedData(session, Country, loadCountries, "data/countries.csv", "Countries")
        SeedData(session, City, loadCities, "data/cities.csv", "Cities")
        SeedData(session, Airport, loadAirports, "data/airports.csv", "Airports")
