class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_plant()-> None:
    raise PlantError("The tomato plant is wilting!")

def check_watering()-> None:
    raise WaterError("Not enough water in the tank!")

def test_custom_errors()-> None:
    
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")

    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    
    print("Testing WaterError...")

    try:
        check_watering()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    
    print("Testing catching all garden errors...")
    for test in [check_plant, check_watering]:
        try:
            test()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()