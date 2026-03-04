"""Build a simple analytics dashboard using comprehensions."""

Player = dict[str, object]
Event = dict[str, object]

if __name__ == "__main__":
    players: list[Player] = [
        {"name": "alice", "score": 2300, "active": True},
        {"name": "bob", "score": 1800, "active": True},
        {"name": "charlie", "score": 2150, "active": True},
        {"name": "diana", "score": 2050, "active": False},
    ]

    player_achievements: dict[str, list[str]] = {
        "alice": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "first_kill",
            "level_10",
        ],
        "bob": [
            "first_kill",
            "level_10",
            "first_kill",
        ],
        "charlie": [
            "boss_slayer",
            "level_10",
            "first_kill",
            "first_kill",
            "level_10",
            "boss_slayer",
            "level_10",
        ],
        "diana": [
            "first_kill",
            "level_10",
        ],
    }

    events: list[Event] = [
        {"region": "north", "active": True},
        {"region": "east", "active": True},
        {"region": "central", "active": True},
        {"region": "north", "active": True},
        {"region": "west", "active": False},
    ]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    high_scorers: list[str] = [
        str(player["name"])
        for player in players
        if int(player["score"]) > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores: list[int] = [
        int(player["score"]) * 2
        for player in players
    ]
    print(f"Scores doubled: {doubled_scores}")

    active_players: list[str] = [
        str(player["name"])
        for player in players
        if bool(player["active"])
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    players_score: dict[str, int] = {
        str(player["name"]): int(player["score"])
        for player in players
    }
    print(f"Players Score: {players_score}")

    score_categories: dict[str, int] = {
        "high": sum(
            [
                1
                for player in players
                if int(player["score"]) >= 2100
            ]
        ),
        "medium": sum(
            [
                1
                for player in players
                if 1900 <= int(player["score"]) < 2100
            ]
        ),
        "low": sum(
            [
                1
                for player in players
                if int(player["score"]) < 1900
            ]
        ),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        player_name: len(player_achievements[player_name])
        for player_name in player_achievements
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = {
        str(player["name"])
        for player in players
    }
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = {
        achievement
        for player_name in player_achievements
        for achievement in player_achievements[player_name]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {
        str(event["region"])
        for event in events
        if bool(event["active"]) is True
    }
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players: int = len(players)
    print(f"Total players: {total_players}")

    total_unique_achievements: int = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    scores: list[int] = [
        int(player["score"])
        for player in players
    ]
    average_score: float = sum(scores) / len(scores)
    print(f"Average score: {average_score}")

    top_score: int = max(scores)

    top_name: str = [
        str(player["name"])
        for player in players
        if int(player["score"]) == top_score
    ][0]

    top_achievements: int = len(player_achievements[top_name])

    print(
        f"Top performer: {top_name} "
        f"({top_score} points, "
        f"{top_achievements} achievements)"
    )
