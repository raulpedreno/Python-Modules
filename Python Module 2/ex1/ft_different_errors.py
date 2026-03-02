def garden_operations() -> None:
    """Demonstrate different Python error types using garden examples."""

    print("=== Garden Error Types Demo ===\n")

    # ValueError
    try:
        print("Testing ValueError...")
        int("abc")  # number: int = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    # ZeroDivisionError
    try:
        print("Testing ZeroDivisionError...")
        10 / 0  # result = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    # FileNotFoundError
    try:
        print("Testing FileNotFoundError...")
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    # KeyError
    try:
        print("Testing KeyError...")
        plants = {"rose": 5}
        plants["missing_plant"]  # value = plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    # Multiple errors
    try:
        print("Testing multiple errors together...")
        int("abc")  # num: int = int("abc")
        5 / 0  # result = 5 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


def test_error_types() -> None:
    """Run the garden error demonstration."""
    garden_operations()


if __name__ == "__main__":
    test_error_types()
