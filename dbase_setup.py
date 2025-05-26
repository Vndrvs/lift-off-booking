from data_init.database_initializer import InitializeDatabase
from data_init.seed_data_initializer import RunSeeding
from data_init.model_data_initializer import LoadAllData

def RunSetup():

    print("1. Initializing the database\n")
    InitializeDatabase() 

    print("2. Seeding the sample data\n")
    RunSeeding()

    print("3. Loading the models\n")
    LoadAllData()

    print("Thanks for the patience. The database is up and running.")