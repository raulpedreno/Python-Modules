from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana: int,
    ):
        super().__init__(name, cost, rarity)

        if attack_power <= 0:
            raise ValueError("Attack power must be positive")
        if health <= 0:
            raise ValueError("Health must be positive")
        if mana < 0:
            raise ValueError("Mana cannot be negative")

        self.attack_power = attack_power
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card played",
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict:
        remaining = max(self.health - incoming_damage, 0)
        return {
            "defender": self.name,
            "incoming_damage": incoming_damage,
            "remaining_health": remaining,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount,
            "mana": self.mana,
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana,
        }
