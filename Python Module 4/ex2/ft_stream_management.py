"""Demonstrate input, output, and error stream usage."""

import sys


def main() -> None:
    """Collect input and send messages through the correct streams."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")

    print()

    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
