from model_loaders.load_airlines import CreateModelDictionary

def PrintTest():
    csv_path = "data/airlines.csv"
    
    airlines_by_id = CreateModelDictionary(csv_path)
    
    for id, airline in airlines_by_id.items():
        print(f"{id}, {airline.name}, {airline.hqCityId}")

PrintTest()