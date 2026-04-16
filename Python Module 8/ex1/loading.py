import importlib
import os
from types import ModuleType
from typing import Tuple, Dict, Optional


def check_dependency(name: str) -> Tuple[bool, Optional[ModuleType]]:
    """
    Attempts to dynamically import a module.
    Returns (True, module) if found, or (False, None) if missing.
    """
    try:
        module = importlib.import_module(name)
        return True, module
    except ImportError:
        return False, None


def show_dependency_status() -> Dict[str, Optional[ModuleType]]:
    """
    Checks pandas, numpy and matplotlib.
    Displays their version if they are installed.
    """
    print("Checking dependencies:\n")

    dependencies = ["pandas", "numpy", "matplotlib"]
    loaded: Dict[str, Optional[ModuleType]] = {}

    for dep in dependencies:
        ok, module = check_dependency(dep)
        if ok:
            print(f"[OK] {dep} ({module.__version__}) - Ready")
            loaded[dep] = module
        else:
            print(f"[MISSING] {dep} - Install it with pip or Poetry")
            loaded[dep] = None

    print()
    return loaded


def detect_environment_manager() -> str:
    """
    Detects whether the script is running under Poetry or pip.
    Poetry sets the POETRY_ACTIVE environment variable when active.
    """
    if os.environ.get("POETRY_ACTIVE"):
        return "Poetry environment detected (pyproject.toml)"
    return "Pip/system environment detected (requirements.txt)"


def create_matrix_dataframe(np, pd):
    """
    Generates simulated data using numpy as the required data source.
    """
    alimentos = ["Avena", "Manzana", "Pollo", "Aguacate", "Lentejas"]

    proteina = np.random.uniform(0, 30, size=5)
    fibra = np.random.uniform(0, 10, size=5)
    grasas = np.random.uniform(0, 20, size=5)
    azucares = np.random.uniform(0, 15, size=5)

    df = pd.DataFrame({
        "alimento": alimentos,
        "proteina": proteina,
        "fibra": fibra,
        "grasas": grasas,
        "azucares": azucares
    })

    df["indice_saciedad"] = (
        0.4 * df["proteina"] +
        0.4 * df["fibra"] +
        0.2 * df["grasas"] -
        0.3 * df["azucares"]
    )

    return df


def plot_matrix(df):
    """
    Generates a bar chart and saves it as matrix_analysis.png.
    """
    # IMPORTACIÓN CORRECTA DE PYLOT
    plt = importlib.import_module("matplotlib.pyplot")

    df_sorted = df.sort_values(by="indice_saciedad", ascending=False)

    plt.figure(figsize=(8, 5))
    plt.bar(df_sorted["alimento"], df_sorted["indice_saciedad"], color="cyan")

    plt.title("Matrix Data — Índice de Saciedad")
    plt.xlabel("Alimento")
    plt.ylabel("Índice de saciedad")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("Visualization saved as matrix_analysis.png\n")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")

    loaded = show_dependency_status()

    if None in loaded.values():
        print("ERROR: Missing dependencies detected.")
        print("Install them using pip or Poetry and run again.\n")
        exit(1)

    pd = loaded["pandas"]
    np = loaded["numpy"]

    print(detect_environment_manager(), "\n")

    print("Analyzing Matrix data...")
    df = create_matrix_dataframe(np, pd)
    print("Processing simulated data...\n")

    plot_matrix(df)

    print("Analysis complete!")
