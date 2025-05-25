# this py is currently used for testing the model loaders

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath("."))

from app.model_loaders.load_airlines import CreateModelDictionary

if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "data", "airlines.csv")
    airlines_by_id = CreateModelDictionary(path)

    for id, airline in airlines_by_id.items():
        print(f"{id}, {airline.name}, {airline.hqCityId}")