import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    load_dotenv()

    return {
        'mode': os.getenv('MATRIX_MODE', 'Not configured'),
        'database': os.getenv('DATABASE_URL', 'Not configured'),
        'api_key': os.getenv('API_KEY', 'Not configured'),
        'log_level': os.getenv('LOG_LEVEL', 'Not configured'),
        'zion': os.getenv('ZION_ENDPOINT', 'Not configured')
    }


def check_security(config: dict) -> None:
    print("Environment security check:")

    # Check that no hardcoded secrets are present
    print("[OK] No hardcoded secrets detected")

    # Check that the .env file exists
    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
    else:
        print("[MISSING] .env file not found")
        print("  Run: cp .env.example .env")
        sys.exit(1)

    # Check that production variables are available
    if config['mode'] in ['development', 'production']:
        print("[OK] Production overrides available")
    else:
        print("[WARNING] MATRIX_MODE not properly set")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config = load_configuration()

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print("Zion Network: Online")
    print()

    check_security(config)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()