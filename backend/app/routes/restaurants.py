from fastapi import APIRouter
from app.services.data_service import load_restaurants
from app.services.restaurant_search import filter_restaurants
from app.services.ai_recommendation import extract_preferences
from app.services.recommendation_service import score_restaurants

router = APIRouter()

restaurants = load_restaurants()


@router.get("/")
def get_restaurants():
    return restaurants


@router.get("/recommend")
def recommend_restaurant(query: str):
    preferences = extract_preferences(query)

    results = score_restaurants(
        restaurants,
        preferences
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