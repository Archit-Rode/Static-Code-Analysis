import json
from datetime import datetime
import ast


def add_item(stock_data, item, qty, logs=None):
    """Add an item and quantity to the stock data with validation."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        raise ValueError("Item name must be a string.")
    if not isinstance(qty, int) or qty < 0:
        raise ValueError("Quantity must be a non-negative integer.")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs


def remove_item(stock_data, item, qty):
    """Remove a quantity of an item from stock with safe handling."""
    try:
        if item in stock_data and stock_data[item] >= qty:
            stock_data[item] -= qty
            if stock_data[item] == 0:
                del stock_data[item]
        else:
            print(f"Cannot remove {qty} of {item}: insufficient stock.")
    except KeyError as e:
        print(f"Error removing {item}: {e}")


def get_qty(stock_data, item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(filename="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading file: {e}")
        return {}


def save_data(stock_data, filename="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except (OSError, TypeError) as e:
        print(f"Error saving file: {e}")


def safe_parse_command(command_str):
    """Safely parse a string into a Python object (no eval!)."""
    try:
        return ast.literal_eval(command_str)
    except (ValueError, SyntaxError) as e:
        print(f"Invalid command: {e}")
        return None


def print_data(stock_data):
    """Print all items in stock."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def main():
    """Demonstrate inventory system operations."""
    stock_data = load_data()
    logs = []

    # Add and remove items safely
    logs = add_item(stock_data, "apple", 10, logs)
    logs = add_item(stock_data, "banana", 5, logs)
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    # Print current stock
    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print_data(stock_data)

    # Save updated stock
    save_data(stock_data)

    # Example safe parsing instead of eval
    command = safe_parse_command("{'action': 'add', 'item': 'pear', 'qty': 4}")
    if command:
        print(f"Safe parsed command: {command}")


if __name__ == "__main__":
    main()
