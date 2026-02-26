def check_temperature(temp_str: str) -> int:
    """Validate temperature input and return a valid integer value."""

    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature_input() -> None:
    """Demonstrate temperature validation with different inputs."""

    print("=== Garden Temperature Checker ===\n")

    test_values: list[str] = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Testing temperature: {value}")

        try:
            result: int = check_temperature(value)
            print(f"Temperature {result}°C is perfect for plants!")

        except ValueError as error:
            print(f"Error: {error}")

        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
