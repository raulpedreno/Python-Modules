from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        valid_types = {"damage", "heal", "buff", "debuff"}
        if effect_type not in valid_types:
            raise ValueError("Invalid effect type")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.effect_type} spell resolved",
            "consumed": True,
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Spell",
            "effect_type": self.effect_type,
        })
        return info
