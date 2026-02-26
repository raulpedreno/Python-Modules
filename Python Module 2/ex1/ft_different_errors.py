def garden_operations()-> None:
    print("=== Garden Error Types Demo ===\n")

##ValueEror
    try:
        print("Testing ValueError...")
        number = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

##ZeroDivisionError
    try:
        print("Testing ZeroDivisionError...")
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

##FileNotFoundError
    try:
        print("Testing FileNotFoundError...")
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

##Testing KeyError
    try:
        print("Testing KeyError...")
        plants = {"rose" : 5}
        value = plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

##Multiple errors
    try:
        print("Testing multiple errors together...")
        num = int("abc")
        result = 5 / 0
    except(ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")

def test_error_types()-> None:
    garden_operations()


if __name__ == "__main__":
    test_error_types()
