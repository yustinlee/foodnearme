import json
from pathlib import Path


def load_restaurants():
    data_path = Path(__file__).parent.parent / "data" / "restaurants.json"

    with open(data_path, "r") as file:
        return json.load(file)