import json
import os

def load_json(filepath, default=None):
    if not os.path.exists(filepath):
        return default if default is not None else []
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        return default if default is not None else []

def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def load_state(data_dir):
    tables = load_json(os.path.join(data_dir, 'tables.json'), [])
    menu = load_json(os.path.join(data_dir, 'menu.json'), {})
    orders = load_json(os.path.join(data_dir, 'orders.json'), {})
    return tables, menu, orders

def save_state(data_dir, tables, menu, orders):
    save_json(os.path.join(data_dir, 'tables.json'), tables)
    save_json(os.path.join(data_dir, 'menu.json'), menu)
    save_json(os.path.join(data_dir, 'orders.json'), orders)
