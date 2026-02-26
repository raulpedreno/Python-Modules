class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        # nombre -> (water_level, sunlight_hours)
        self.plants: dict[str, tuple[int, int]] = {}

    def add_plant(self, name: str, water: int, sun: int) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")

        self.plants[name] = (water, sun)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")

            for name in self.plants:
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found!")

        water, sun = self.plants[name]

        if water < 1 or water > 10:
            raise PlantError(
                f"Water level {water} is invalid (must be between 1 and 10)"
            )

        if sun < 2 or sun > 12:
            raise PlantError(
                f"Sunlight hours {sun} are invalid (must be between 2 and 12)"
            )

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    for data in [("tomato", 5, 8), ("lettuce", 15, 6), ("", 4, 5)]:
        try:
            manager.add_plant(*data)
        except PlantError as error:
            print(f"Error adding plant: {error}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nChecking plant health...")
    for name in ["tomato", "lettuce"]:
        try:
            manager.check_plant_health(name)
        except GardenError as error:
            print(f"Error checking {name}: {error}")

    print("\nTesting error recovery...")
    empty_manager = GardenManager()
    try:
        empty_manager.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()