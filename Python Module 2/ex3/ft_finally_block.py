def water_plants(plant_list) -> None:
    """Water each plant in the list and handle invalid entries."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Run several watering tests to demonstrate error handling."""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    plants = ["Rose", "Tulip", None, "Daisy"]
    water_plants(plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
