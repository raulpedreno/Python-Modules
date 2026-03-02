class Plant:
    """Represent a plant with its name, height, and age in days."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def create_object(self) -> None:
        """Print a message confirming the plant has been created."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    for plant in plants:
        plant.create_object()

    print(f"\nTotal plants created: {len(plants)}")
