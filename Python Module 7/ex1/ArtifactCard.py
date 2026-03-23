from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str,
            durability: int, effect: str):
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability,
            "activated": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        })
        return info
