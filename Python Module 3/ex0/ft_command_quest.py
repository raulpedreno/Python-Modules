import sys


if __name__ == "__main__":
    print("=== Command Quest ===")

    args: list[str] = sys.argv

    if len(args) == 1:
        print("No arguments provided!")
    print(f"Program name: {args[0]}")

    if len(args) > 1:
        print(f"Arguments received: {len(args) - 1}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")

    print("Total arguments: ", len(args))