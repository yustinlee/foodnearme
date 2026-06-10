from fastapi import APIRouter

from app.services.restaurant_search import filter_restaurants
from app.services.ai_recommendation import extract_preferences

router = APIRouter()

restaurants = [
    {
        "id": 1,
        "name": "Taco House",
        "cuisine": "Mexican",
        "budget": 1,
        "rating": 4.3
    },
    {
        "id": 2,
        "name": "Sushi Place",
        "cuisine": "Japanese",
        "budget": 3,
        "rating": 4.8
    },
    {
        "id": 3,
        "name": "Burger Spot",
        "cuisine": "American",
        "budget": 2,
        "rating": 4.1
    }
]


@router.get("/")
def get_restaurants():
    return restaurants


@router.get("/recommend")
def recommend_restaurant(query: str):
    preferences = extract_preferences(query)

    results = filter_restaurants(
        restaurants,
        cuisine=preferences.get("cuisine"),
        budget=preferences.get("budget")
    )

    return {
        "query": query,
        "preferences": preferences,
        "results": results
    }


@router.get("/search")
def search_restaurants(
    cuisine: str | None = None,
    budget: int | None = None
):
    return filter_restaurants(
        restaurants,
        cuisine=cuisine,
        budget=budget
    )


@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    return {"error": "Restaurant not found"}