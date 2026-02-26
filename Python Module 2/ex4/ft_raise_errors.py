def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> str:
    # Check plant name
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    # Check water level
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    # Check sunlight hours
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    # Good values
    try:
        print("Testing good values...")
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

    # Empty plant name
    try:
        print("Testing empty plant name...")
        result = check_plant_health("", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

    # Bad water level
    try:
        print("Testing bad water level...")
        result = check_plant_health("tomato", 15, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

    # Bad sunlight hours
    try:
        print("Testing bad sunlight hours...")
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()