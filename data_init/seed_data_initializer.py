# this module is responsible for populating the database with base and / or testing data
# hence the name, seeder

from sqlalchemy.orm import Session
from data_init.seeders.country_seeder import loadCountries
from data_init.seeders.city_seeder import loadCities
from data_init.seeders.airport_seeder import loadAirports
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from data_init.database_initializer import Country, City, Airport, engine
from utils.insert_logger import Logger

# generic function for loading records from csv files
# params: 1. session 2. model (class) 3. loader function type 4. filepath 5. name of class
def SeedData(session, model, loader, path, category) -> int:

    recordCount = 0

    records = loader(path)

    if not records:
        print(f"0 {category.lower()} found.")
        return

    try:
        # if the loader encounters records with name fields that already exist in the dbase, it skips them
        stmt = sqlite_insert(model).values(records).on_conflict_do_nothing(index_elements=["name"])
        result = session.execute(stmt)
        session.commit()
        
        recordCount = result.rowcount

        return recordCount

    except Exception as e:
        session.rollback()
        print(f"Insertion error for {category.lower()}: {e}")

# initializing the component for all the non-class type records

def RunSeeding():
    seedParams = [
        (Country, loadCountries, "data/countries.csv", "Countries"),
        (City, loadCities, "data/cities.csv", "Cities"),
        (Airport, loadAirports, "data/airports.csv", "Airports"),
    ]

    with Session(bind=engine) as session:
        for model, loader, path, category in seedParams:
            insertedCount = SeedData(session, model, loader, path, category)
            Logger(insertedCount, category)
    
    print()