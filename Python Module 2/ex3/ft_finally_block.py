def water_plants(plant_list)-> None:
    print("Opening watering system...")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")

            print(f"Watering {plant}...")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system()-> None:
    print("=== Garden Watering System ===")

    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)

    print("Watering system test completed!")
    
    print()

    plants = ["Rose", "Tulip", None, "Daisy"]
    water_plants(plants)

    print("Watering system test completed!")
    
if __name__ == "__main__":
    test_watering_system()

