"""Recover data from the ancient archive fragment."""


def main() -> None:
    """Read and display the ancient archive contents."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        file = open("ancient_fragment.txt", "r")
        data: str = file.read()
        print("RECOVERED DATA:")
        print(data)
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
