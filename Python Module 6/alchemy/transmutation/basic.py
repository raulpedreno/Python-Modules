

def lead_to_gold() -> str:
    """Return a lead-to-gold transmutation string."""
    from alchemy.elements import create_fire
    fire_result = create_fire()
    return f"Lead transmuted to gold using {fire_result}"


def stone_to_gem() -> str:
    """Return a stone-to-gem transmutation string."""
    from alchemy.elements import create_earth
    earth_result = create_earth()
    return f"Stone transmuted to gem using {earth_result}"
