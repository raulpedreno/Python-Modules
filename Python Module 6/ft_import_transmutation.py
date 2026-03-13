import alchemy
import alchemy.elements
from alchemy.elements import create_earth, create_fire, create_water
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion as strength


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    try:
        print(
            f"alchemy.elements.create_fire(): "
            f"{alchemy.elements.create_fire()}"
        )
    except AttributeError:
        print("Error")

    print("\nMethod 2 - Specific function import:")
    try:
        print(f"create_water(): {create_water()}")
    except AttributeError:
        print("Error")

    print("\nMethod 3 - Aliased import:")
    try:
        print(f"heal(): {heal()}")
    except AttributeError:
        print("Error")

    print("\nMethod 4 - Multiple imports:")
    try:
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength()}")
    except AttributeError:
        print("Error")

    print("\nAll import transmutation methods mastered!")
