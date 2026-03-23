from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    deck = Deck()

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn")

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print("Deck stats:")
    print(deck.get_deck_stats())

    deck.shuffle()

    print("\nDrawing and playing cards:\n")
    while deck.cards:
        card = deck.draw_card()
        print(f"Drew: {card.name} ({type(card).__name__})")
        print("Play result:", card.play({}))
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
