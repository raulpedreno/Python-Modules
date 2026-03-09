"""Handle archive access failures with crisis response protocols."""


def crisis_handler(filename: str) -> None:
    """Try to recover an archive and handle access failures."""
    try:
        with open(filename, "r") as file:
            content: str = file.read().strip()
            print(f'SUCCESS: Archive recovered - "{content}"')
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled")


def main() -> None:
    """Run all crisis response scenarios."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler("lost_archive.txt")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    crisis_handler("classified_vault.txt")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
