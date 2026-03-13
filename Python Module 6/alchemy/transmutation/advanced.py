

def philosophers_stone() -> str:
    """Return a philosopher's stone creation string."""
    from .basic import lead_to_gold
    from ..potions import healing_potion

    lead_to_gold_result = lead_to_gold()
    healing_potion_result = healing_potion()
    return (
        f"Philosopher’s stone created using {lead_to_gold_result} " +
        f"and {healing_potion_result}"
    )


def elixir_of_life() -> str:
    """Return an elixir of life string."""
    return "Elixir of life: eternal youth achieved!"
