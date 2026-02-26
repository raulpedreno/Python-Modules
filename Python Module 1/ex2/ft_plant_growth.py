class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self, cm: int) -> None:
        self.height += cm

    def age(self) -> None:
        self.age_days += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def grow_in_days(height_last_day: int, height_day_one: int) -> None:
    growth: int = height_last_day - height_day_one
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 18, 12),
        Plant("Lily", 20, 5),
    ]

    print("=== Day 1 ===")

    # Guardamos alturas iniciales
    day_one_heights: list[int] = []
    for plant in plants:
        plant.get_info()
        day_one_heights.append(plant.height)

    # Simulamos 6 días de crecimiento
    for _ in range(6):
        for plant in plants:
            plant.grow(2)
            plant.age()

    print("=== Day 7 ===")

    for i in range(len(plants)):
        plants[i].get_info()
        grow_in_days(plants[i].height, day_one_heights[i])