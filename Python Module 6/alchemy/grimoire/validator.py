def validate_ingredients(ingredients: str) -> str:
    """Return VALID or INVALID depending on ingredient content."""
    valid_tokens = ["fire", "water", "earth", "air"]
    is_valid = any(token in ingredients for token in valid_tokens)

    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
