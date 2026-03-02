class Plant:
    """Represents a basic plant with a name and height."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with its name and height."""
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Increase the plant's height by 1 cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Represents a plant that produces flowers and has a color."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with a color."""
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """Represents a special flower that awards prize points."""

    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int
    ) -> None:
        """Initialize a prize flower with additional prize points."""
        super().__init__(name, height, color)
        self.prize_points = prize_points


class Garden:
    """Represents a garden that contains multiple plants."""

    def __init__(self, owner_name: str) -> None:
        """Create an empty garden owned by a specific person."""
        self.owner_name = owner_name
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        self.plants_added: int = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and update the counter."""
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self) -> None:
        """Make all plants in the garden grow by 1 cm."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        """Display a detailed report of all plants in the garden."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                )
            elif isinstance(plant, FloweringPlant):
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming)"
                )
            else:
                print(f"- {plant.name}: {plant.height}cm")

    def check_height(self) -> bool:
        """Verify that all plants have a valid (non-negative) height."""
        for plant in self.plants:
            if not GardenManager.validate_height_value(plant.height):
                return False
        return True


class GardenManager:
    """Manages multiple gardens and provides statistical tools."""

    def __init__(self) -> None:
        """Initialize the manager with an empty list of gardens."""
        self.gardens: list[Garden] = []
        self.stats = self.GardenStats()

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager."""
        self.gardens.append(garden)

    @staticmethod
    def validate_height_value(height: int) -> bool:
        """Return True if the height is valid (non-negative)."""
        return height >= 0

    class GardenStats:
        """Provides statistical calculations for gardens."""

        def count_plants(self, garden: Garden) -> int:
            """Return the number of plants in the garden."""
            return len(garden.plants)

        def average_height(self, garden: Garden) -> float:
            """Calculate the average height of plants in the garden."""
            if len(garden.plants) == 0:
                return 0.0
            total: int = 0
            for plant in garden.plants:
                total += plant.height
            return total / len(garden.plants)

        def total_prize_points(self, garden: Garden) -> int:
            """Sum all prize points from prize flowers in the garden."""
            total: int = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    total += plant.prize_points
            return total

        def count_by_type(self, garden: Garden) -> dict[str, int]:
            """Count how many plants belong to each plant category."""
            count_plant = 0
            count_flower = 0
            count_prize = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    count_prize += 1
                elif isinstance(plant, FloweringPlant):
                    count_flower += 1
                else:
                    count_plant += 1

            return {
                "regular": count_plant,
                "flowering": count_flower,
                "prize": count_prize
            }

        def garden_score(self, garden: Garden) -> int:
            """Calculate the garden's score based on height and prize points"""
            total_height: int = 0
            for plant in garden.plants:
                total_height += plant.height
            prize_points = self.total_prize_points(garden)
            return total_height + prize_points

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Create a manager with two example gardens and sample plants."""
        manager = cls()

        garden1 = Garden("Alice")
        manager.add_garden(garden1)
        garden1.add_plant(Plant("Oak Tree", 100))
        garden1.add_plant(FloweringPlant("Rose", 25, "red"))
        garden1.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

        garden2 = Garden("Bob")
        manager.add_garden(garden2)
        garden2.add_plant(Plant("Cactus", 10))
        garden2.add_plant(FloweringPlant("Daisy", 12, "white"))
        garden2.add_plant(PrizeFlower("Orchid", 18, "purple", 7))

        return manager


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    print()

    for garden in manager.gardens:
        garden.grow_all()

    print()

    for garden in manager.gardens:
        garden.report()

    for garden in manager.gardens:
        total = manager.stats.count_plants(garden)
        print(f"Plants added: {total}, Total growth: {garden.total_growth}cm")

    for garden in manager.gardens:
        types = manager.stats.count_by_type(garden)
        print(
            f"Plant types: {types['regular']} regular, "
            f"{types['flowering']} flowering, "
            f"{types['prize']} prize flowers"
        )

    print()

    for garden in manager.gardens:
        check = garden.check_height()
        print(f"Height validation test: {check}")

    scores: dict[str, int] = {}
    for garden in manager.gardens:
        scores[garden.owner_name] = manager.stats.garden_score(garden)

    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
    print(f"Total gardens managed: {len(manager.gardens)}")
