from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Epic",
        attack_power=5,
        health=10,
        mana=7,
    )

    print("Combat phase:")
    print("Attack:", elite.attack("Enemy"))
    print("Defend:", elite.defend(3))
    print("Combat stats:", elite.get_combat_stats())

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana Channel:", elite.channel_mana(2))
    print("Magic stats:", elite.get_magic_stats())

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
