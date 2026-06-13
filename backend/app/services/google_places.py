import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

URL = "https://places.googleapis.com/v1/places:searchNearby"


def search_restaurants(latitude, longitude, radius=5000):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": (
            "places.displayName,"
            "places.formattedAddress,"
            "places.rating,"
            "places.priceLevel,"
            "places.types"
        )
    }

    payload = {
        "includedTypes": ["restaurant"],
        "maxResultCount": 20,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "radius": radius
            }
        }
    }

    response = requests.post(
        URL,
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    return response.json().get("places", [])