class GardenError(Exception):
    """Base class for all garden-related custom errors."""
    pass


class PlantError(GardenError):
    """Error raised when a plant-related issue occurs."""
    pass


class WaterError(GardenError):
    """Error raised when a watering-related issue occurs."""
    pass


class GardenManager:
    """Manage plants and validate their water and sunlight levels."""

    def __init__(self) -> None:
        """Initialize the manager with an empty plant dictionary."""
        self.plants: dict[str, tuple[int, int]] = {}

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """Add a plant with its water and sunlight requirements."""
        if not name:
            raise PlantError("Plant name cannot be empty!")

        self.plants[name] = (water, sun)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plants, raising an error if none exist."""
        print("Opening watering system")

        if not self.plants:
            raise WaterError("Not enough water in tank")
        try:
            for name in self.plants:
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        """Validate the health of a specific plant."""
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found!")

        water, sun = self.plants[name]

        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")

        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} are too low (min 2)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} are too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """Run a full demonstration of garden management operations."""
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
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
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
