class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points


class Garden:
    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        self.plants_added: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(
                    f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                )
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")

    def check_height(self) -> bool:
        for plant in self.plants:
            if not GardenManager.validate_height_value(plant.height):
                return False
        return True


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []
        self.stats = self.GardenStats()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    @staticmethod
    def validate_height_value(height: int) -> bool:
        return height >= 0

    class GardenStats:
        def count_plants(self, garden: Garden) -> int:
            return len(garden.plants)

        def average_height(self, garden: Garden) -> float:
            if len(garden.plants) == 0:
                return 0.0
            total: int = 0
            for plant in garden.plants:
                total += plant.height
            return total / len(garden.plants)

        def total_prize_points(self, garden: Garden) -> int:
            total: int = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    total += plant.prize_points
            return total

        def count_by_type(self, garden: Garden) -> dict[str, int]:
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

            return {"regular": count_plant, "flowering": count_flower, "prize": count_prize}

        def garden_score(self, garden: Garden) -> int:
            total_height: int = 0
            for plant in garden.plants:
                total_height += plant.height
            prize_points = self.total_prize_points(garden)
            return total_height + prize_points

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        manager = cls()

        # Garden of Alice
        garden1 = Garden("Alice")
        manager.add_garden(garden1)

        garden1.add_plant(Plant("Oak Tree", 100))
        garden1.add_plant(FloweringPlant("Rose", 25, "red"))
        garden1.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

        # Garden of Bob (añadido para que el demo sea realmente multi-garden)
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
