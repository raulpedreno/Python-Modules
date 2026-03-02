class SecurePlant:
    """A plant with protected attributes that can only be modified safely."""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with private name, height, and age."""
        self.__name = name
        self.__height = height
        self.__age = age

    def set_height(self, value: int) -> None:
        """Safely update the plant's height, rejecting negative values."""
        if value < 0:
            print(
                f"\nInvalid operation attempted: height {value}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, value: int) -> None:
        """Safely update the plant's age, rejecting negative values."""
        if value < 0:
            print(f"\nInvalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        """Return the plant's current height."""
        return self.__height

    def get_age(self) -> int:
        """Return the plant's current age in days."""
        return self.__age

    def get_name(self) -> str:
        """Return the plant's name."""
        return self.__name

    def current_plant(self) -> None:
        """Print the plant's current state in a readable format."""
        print(
            f"\nCurrent plant: {self.__name}",
            f"({self.__height}cm, {self.__age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 15)
    print(f"Plant created: {rose.get_name()}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.current_plant()
