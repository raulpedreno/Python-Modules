from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    creatureCard = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(creatureCard.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {creatureCard.is_playable(6)}")

    game_state = {}
    print(f"Play result: {creatureCard.play(game_state)}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creatureCard.attack_target('Goblin Warrior')}\n")

    creatureCard = CreatureCard("Fire Dragon", 2, "Legendary", 7, 5)
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {creatureCard.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
