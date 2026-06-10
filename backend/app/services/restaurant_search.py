
def filter_restaurants(
    restaurants,
    cuisine=None,
    budget=None
):
    results = []

    for restaurant in restaurants:
        if cuisine is not None:
            if restaurant["cuisine"].lower() != cuisine.lower():
                continue

        if budget is not None:
            if restaurant["budget"] != budget:
                continue

        results.append(restaurant)

    return results