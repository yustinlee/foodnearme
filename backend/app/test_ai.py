from services.ai_recommendation import extract_preferences
from services.google_places import search_restaurants
results = search_restaurants(
    latitude=34.536,
    longitude=-117.292
)

for restaurant in results:
    print(
        restaurant.get("displayName", {}).get("text"),
        restaurant.get("rating")
    )