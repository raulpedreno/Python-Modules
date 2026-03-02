class Plant:
    """Base class representing a generic plant with name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with basic attributes."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flower, extending Plant with a color attribute."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with name, height, age and color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def show_info_flower(self) -> None:
        """Display detailed information about the flower."""
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    """Represents a tree, extending Plant with trunk diameter."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        """Initialize a tree with name, height, age and trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and print the amount of shade the tree provides."""
        shade: float = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade} square meters of shade")

    def show_info_tree(self) -> None:
        """Display detailed information about the tree."""
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """Represents a vegetable with harvest season and nutritional value."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """Initialize a vegetable with extra agricultural attributes."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_info_vegetable(self) -> None:
        """Display detailed information about the vegetable."""
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    flowers = [
        Flower("Rose", 25, 30, "red")
    ]

    trees = [
        Tree("Oak", 500, 1825, 50)
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    ]

    for f in flowers:
        f.show_info_flower()
        f.bloom()
    print()
    for t in trees:
        t.show_info_tree()
        t.produce_shade()
    print()
    for v in vegetables:
        v.show_info_vegetable()
