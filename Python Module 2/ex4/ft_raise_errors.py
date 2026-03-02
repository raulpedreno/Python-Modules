def check_plant_health(
    plant_name,
    water_level: int,
    sunlight_hours: int
) -> str:
    """Validate plant health parameters and return a status message."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Run several tests to demonstrate plant health validation."""
    print("=== Garden Plant Health Checker ===\n")

    try:
        print("Testing good values...")
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")
    print()
    try:
        print("Testing empty plant name...")
        result = check_plant_health("", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")
    print()
    try:
        print("Testing bad water level...")
        result = check_plant_health("tomato", 15, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")
    print()
    try:
        print("Testing bad sunlight hours...")
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
