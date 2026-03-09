"""Handle secure archive extraction and preservation."""


def secure_extraction() -> None:
    """Read classified archive data using a safe context manager."""
    print("SECURE EXTRACTION:")
    try:
        with open("archivo.txt", "r") as file:
            for line in file:
                clean_line: str = line.strip()
                print("[CLASSIFIED]", clean_line)
    except FileNotFoundError:
        print("[ERROR] No classified file found for extraction")


def secure_preservation() -> None:
    """Write protected archive data using a safe context manager."""
    print("SECURE PRESERVATION:")
    with open("archivo.txt", "w") as file:
        file.write("Quantum encryption keys recovered\n")
        file.write("Archive integrity: 100%\n")
        file.write("New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")


def main() -> None:
    """Run the vault security workflow."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    secure_extraction()
    print()
    secure_preservation()

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
