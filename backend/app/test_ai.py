from services.ai_recommendation import extract_preferences

test_inputs = [
    "I want cheap sushi near me",
    "fancy italian restaurant for a date night",
    "something spicy and fast",
    "I don’t know, just good food",
    "budget burgers with friends",
]

for text in test_inputs:
    print("\nINPUT:", text)
    result = extract_preferences(text)
    print("OUTPUT:", result)
    print("-" * 40)