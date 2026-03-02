class GardenError(Exception):
    """Base class for all custom garden-related errors."""
    pass


class PlantError(GardenError):
    """Error raised when a plant-related issue occurs."""
    pass


class WaterError(GardenError):
    """Error raised when a watering-related issue occurs."""
    pass


def check_plant() -> None:
    """Simulate a plant problem by raising PlantError."""
    raise PlantError("The tomato plant is wilting!")


def check_watering() -> None:
    """Simulate a watering problem by raising WaterError."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Demonstrate how custom garden errors are raised and handled."""

    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        check_watering()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    for test in [check_plant, check_watering]:
        try:
            test()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
