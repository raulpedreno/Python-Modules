def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))

def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }

if __name__ == "__main__":

    print("Testing artifact sorter ...")
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "fire"},
        {"name": "Crystal Orb", "power": 85, "type": "arcane"},
        {"name": "Shadow Dagger", "power": 40, "type": "dark"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter ...")
    mages = [
        {"name": "Aeris", "power": 120, "element": "wind"},
        {"name": "Boros", "power": 80, "element": "earth"},
        {"name": "Cyra", "power": 150, "element": "fire"}
    ]
    strong_mages = power_filter(mages, 100)
    print("Mages with power >= 100:", [m["name"] for m in strong_mages])

    print("\nTesting spell transformer ...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats ...")
    stats = mage_stats(mages)
    print("Stats:", stats)
