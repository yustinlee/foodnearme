
def extract_preferences(user_input: str):
    preferences = {}

    text = user_input.lower()

    if "mexican" in text:
        preferences["cuisine"] = "Mexican"

    elif "japanese" in text:
        preferences["cuisine"] = "Japanese"

    elif "american" in text:
        preferences["cuisine"] = "American"

    if "cheap" in text:
        preferences["budget"] = 1

    elif "expensive" in text:
        preferences["budget"] = 3

    return preferences