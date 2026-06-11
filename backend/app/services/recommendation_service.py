def score_restaurants(restaurants, preferences):
    scored_restaurants = []

    for restaurant in restaurants:
        score = 0
        score += restaurant["rating"] / 2

        # Cuisine Match
        if preferences.get("cuisine") == restaurant.get("cuisine"):
            score += 3

        # Budget Match
        if preferences.get("budget") == restaurant.get("budget"):
            score += 2

        # Tag Matches
        for tag in preferences.get("tags", []):
            if tag in restaurant.get("tags", []):
                score += 1

                

        restaurant_copy = restaurant.copy()
        restaurant_copy["score"] = score

        scored_restaurants.append(restaurant_copy)

    scored_restaurants.sort(
        key=lambda restaurant: restaurant["score"],
        reverse=True
    )

    return scored_restaurants