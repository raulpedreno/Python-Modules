"""Create a new archive file with preservation entries."""


def main() -> None:
    """Write the required preservation entries to a new archive."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    filename: str = "new_discovery.txt"

    print(f"Initializing new storage unit: {filename}")

    file = open(filename, "w")

    print("Storage unit created successfully...")
    print("Inscribing preservation data...\n")

    entry1: str = "[ENTRY 001] New quantum algorithm discovered\n"
    entry2: str = "[ENTRY 002] Efficiency increased by 347%\n"
    entry3: str = "[ENTRY 003] Archived by Data Archivist trainee\n"

    file.write(entry1)
    file.write(entry2)
    file.write(entry3)

    print("[ENTRY 001] New quantum algorithm discovered")
    print("[ENTRY 002] Efficiency increased by 347%")
    print("[ENTRY 003] Archived by Data Archivist trainee")

    file.close()

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
