

def healing_potion() -> str:
    """Return a healing potion string."""
    from alchemy.elements import create_fire, create_water
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Return a strength potion string."""
    from alchemy.elements import create_earth, create_fire
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Return an invisibility potion string."""
    from alchemy.elements import create_air, create_water
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}")


def wisdom_potion() -> str:
    """Return a wisdom potion string."""
    from alchemy.elements import (
        create_air, create_earth, create_fire, create_water)
    return (
        f"Wisdom potion brewed with {create_fire()}, "
        f"{create_water()}, {create_earth()} and {create_air()}"
    )
