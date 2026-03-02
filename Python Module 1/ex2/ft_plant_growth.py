class Plant:
    """Represent a plant with its name, height, and age in days."""
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self, cm: int) -> None:
        """Increase the plant's height by a given number of centimeters."""
        self.height += cm

    def age(self) -> None:
        """Increase the plant's age by one day."""
        self.age_days += 1

    def get_info(self) -> None:
        """Print a formatted description of the plant's current state."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def grow_in_days(height_last_day: int, height_day_one: int) -> None:
    """Print the growth difference between two recorded heights."""
    growth: int = height_last_day - height_day_one
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 18, 12),
        Plant("Lily", 20, 5),
    ]

    print("=== Day 1 ===")

    day_one_heights: list[int] = []
    for plant in plants:
        plant.get_info()
        day_one_heights.append(plant.height)

    for _ in range(6):
        for plant in plants:
            plant.grow(1)
            plant.age()

    print("=== Day 7 ===")

    for i in range(len(plants)):
        plants[i].get_info()
        grow_in_days(plants[i].height, day_one_heights[i])
