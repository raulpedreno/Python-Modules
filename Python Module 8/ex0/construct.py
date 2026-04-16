import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_env_name() -> str:
    venv_path = os.environ.get('VIRTUAL_ENV', '')
    return os.path.basename(venv_path)


def get_package_paths() -> list[str]:
    try:
        return site.getsitepackages()
    except AttributeError:
        return []


if __name__ == "__main__":

    if is_virtual_env():

        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_env_name()}")
        print(f"Environment Path: {os.environ.get('VIRTUAL_ENV', '')}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation paths:")
        for path in get_package_paths():
            print(f" - {path}")

    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows\n")
        print("Then run this program again.")
