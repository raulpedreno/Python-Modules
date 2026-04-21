from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        boosted_power = power * multiplier
        return base_spell(target, boosted_power)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence_spell


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} energy"

    print("=== Testing spell_combiner ===")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 50))

    print("\n=== Testing power_amplifier ===")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Orc", 10))

    print("\n=== Testing conditional_caster ===")
    strong_only = conditional_caster(lambda t, p: p > 40, fireball)
    print(strong_only("Goblin", 30))
    print(strong_only("Goblin", 60))

    print("\n=== Testing spell_sequence ===")
    seq = spell_sequence([fireball, heal, shield])
    print(seq("Troll", 20))
