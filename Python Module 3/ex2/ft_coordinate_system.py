import math

"""Parse and analyze 3D coordinates using tuples."""


def distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    """Compute Euclidean distance between two 3D points."""
    return math.sqrt(
        (b[0] - a[0]) ** 2
        + (b[1] - a[1]) ** 2
        + (b[2] - a[2]) ** 2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    origin: tuple[int, int, int] = (0, 0, 0)

    # 1️⃣ Create fixed position
    position1: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {position1}")

    distance1: float = distance(origin, position1)
    print(f"Distance between {origin} and {position1}: {distance1:.2f}")

    # 2️⃣ Parse valid coordinates
    coord_string: str = "3,4,0"
    print(f'\nParsing coordinates: "{coord_string}"')

    position2: tuple[int, int, int] | None = None

    try:
        parts: list[str] = coord_string.split(",")
        position2 = (int(parts[0]), int(parts[1]), int(parts[2]))
        print(f"Parsed position: {position2}")

        distance2: float = distance(origin, position2)
        print(f"Distance between {origin} and {position2}: {distance2:.1f}")

    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details - Type: {type(error).__name__}, Args: {error.args}"
        )

    # 3️⃣ Parse invalid coordinates
    invalid_coord: str = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_coord}"')

    try:
        invalid_parts: list[str] = invalid_coord.split(",")
        position3: tuple[int, int, int] = (
            int(invalid_parts[0]),
            int(invalid_parts[1]),
            int(invalid_parts[2]),
        )
        print(f"Parsed position: {position3}")

    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details - Type: {type(error).__name__}, Args: {error.args}"
        )

    # 4️⃣ Tuple unpacking demonstration
    if position2 is not None:
        print("\nUnpacking demonstration:")
        x, y, z = position2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
