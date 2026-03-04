import sys


def join_keys(inventory: dict[str, int]) -> str:
    """Join dictionary keys into a comma-separated string."""
    keys_as_list: list[str] = list(inventory.keys())
    joined_keys: str = ", ".join(keys_as_list)
    return joined_keys


def join_values(inventory: dict[str, int]) -> str:
    """Join dictionary values into a comma-separated string."""
    return ", ".join(str(v) for v in inventory.values())


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")

    if len(sys.argv) == 1:
        print("No inventory provided. Usage: python3 ft_inventory_system.py "
              "item:qty item:qty ...")
        sys.exit(1)

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            name, qty_str = arg.split(":")
            qty: int = int(qty_str)
            inventory[name] = inventory.get(name, 0) + qty
        except ValueError:
            print("Error: invalid input format")
            sys.exit(1)

    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")

    total_items: int = sum(inventory.values())
    for name, qty in inventory.items():
        percentage: float = (qty / total_items) * 100
        print(f"{name}: {qty} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most_item: str = max(inventory, key=inventory.get)
    least_item: str = min(inventory, key=inventory.get)
    print(f"Most abundant: {most_item} ({inventory.get(most_item)} units)")
    print(f"Least abundant: {least_item} ({inventory.get(least_item)} units)")

    print("\n=== Item Categories ===")

    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    for name, qty in inventory.items():
        if qty >= 5:
            moderate[name] = qty
        else:
            scarce[name] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")

    needs_restock: list[str] = []
    for name, qty in inventory.items():
        if qty <= 1:
            needs_restock.append(name)
    print(f"Restock needed: {', '.join(needs_restock)}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {join_keys(inventory)}")
    print(f"Dictionary values: {join_values(inventory)}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
