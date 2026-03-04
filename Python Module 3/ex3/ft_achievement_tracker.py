"""Track and analyze player achievements using sets."""

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }
    bob: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }
    charlie: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    # All unique achievements
    unique_achievements: set[str] = alice.union(bob).union(charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    # Common to all
    inter_achievements: set[str] = (
        alice.intersection(bob).intersection(charlie)
    )
    print(f"\nCommon to all players: {inter_achievements}")

    # Rare achievements
    rare_alice: set[str] = alice.difference(bob).difference(charlie)
    rare_bob: set[str] = bob.difference(alice).difference(charlie)
    rare_charlie: set[str] = charlie.difference(alice).difference(bob)
    rare_all: set[str] = rare_alice.union(rare_bob).union(rare_charlie)
    print(f"Rare achievements (1 player): {rare_all}")

    # Alice vs Bob
    alice_vs_bob_common: set[str] = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {alice_vs_bob_common}")

    alice_unique: set[str] = alice.difference(bob)
    bob_unique: set[str] = bob.difference(alice)
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
