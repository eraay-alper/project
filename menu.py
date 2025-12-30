def initialize_menu(existing_menu=None):
    if existing_menu:
        return existing_menu
    
    return {
        "burger": {"price": 100, "category": "main"},
        "pizza": {"price": 150, "category": "main"},
        "fettuccine alfredo": {"price": 75, "category": "main"},
        "fries": {"price": 35, "category": "starter"},
        "soda": {"price": 20, "category": "beverage"},
        "water": {"price": 10, "category": "beverage"},
        "cola": {"price": 25, "category": "beverage"},
        "energy drink": {"price": 30, "category": "beverage"}
    }

def add_menu_item(menu, name, price, category):
    menu[name.lower()] = {"price": price, "category": category}
    print(f"Added {name} to menu.")
    return menu

def remove_menu_item(menu, name):
    if name.lower() in menu:
        del menu[name.lower()]
        print(f"Removed {name} from menu.")
    else:
        print("Item not found.")
    return menu

def print_menu(menu):
    print(f"{'Item':<20} {'Price':<10} {'Category'}")
    print("-" * 40)
    for name, data in menu.items():
        print(f"{name.title():<20} {data['price']:<10} {data['category']}")
