import typing


Event = tuple[int, str, int, str]


def game_event_stream(n: int) -> typing.Generator[Event, None, None]:
    """Generate n game events on-demand."""
    players: list[str] = ["alice", "bob", "charlie"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]
    levels: list[int] = [5, 12, 8, 3, 14, 7, 10, 1, 9, 6, 11, 2, 13, 4, 15]

    for i in range(1, n + 1):
        player: str = players[(i - 1) % len(players)]
        action: str = actions[(i - 1) % len(actions)]
        level: int = levels[(i - 1) % len(levels)]
        yield i, player, level, action


def fibonacci() -> typing.Generator[int, None, None]:
    """Generate an infinite Fibonacci sequence."""
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> typing.Generator[int, None, None]:
    """Generate an infinite sequence of prime numbers."""
    candidate: int = 2
    while True:
        is_prime: bool = True
        divisor: int = 2

        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            yield candidate

        candidate += 1


def process_stream(n: int) -> None:
    """Process events without storing them."""
    total_events: int = 0
    high_level: int = 0
    treasure_events: int = 0
    level_up_events: int = 0

    for event_id, name, level, action in game_event_stream(n):
        total_events += 1

        if event_id <= 3:
            print(f"Event {event_id}: Player {name} (level {level}) {action}")
        elif event_id == 4:
            print("...")

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: N/A")


def generator_demo() -> None:
    """Demonstrate infinite generators with small samples."""
    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        if i > 0:
            print(", ", end="")
        print(next(fib), end="")
    print()

    prime_gen = primes()
    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        if i > 0:
            print(", ", end="")
        print(next(prime_gen), end="")
    print()


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    events: int = 1000
    print(f"Processing {events} game events...\n")

    # Streaming (no storage)
    process_stream(events)

    # Extra generator demos (like the subject example)
    generator_demo()
