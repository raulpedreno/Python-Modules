def record_spell(spell_name: str, ingredients: str) -> str:
    """Return a spell record string after validation."""
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if validation_result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"

    return f"Spell rejected: {spell_name} ({validation_result})"
