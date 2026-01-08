def open_order(orders, table_number):
    t_str = str(table_number)
    if t_str not in orders:
        orders[t_str] = {'items': [], 'active': True}
    return orders

def add_item_to_order(orders, table_number, menu, item_name, quantity):
    t_str = str(table_number)
    if t_str not in orders or not orders[t_str]['active']:
        print("No active order for this table.")
        return orders
    
    item_key = item_name.lower()
    if item_key not in menu:
        print("Item not on menu.")
        return orders

    price = menu[item_key]['price']
    orders[t_str]['items'].append({
        'name': item_key,
        'quantity': quantity,
        'price': price,
        'status': 'ordered'
    })
    print(f"Added {quantity} x {item_name} to Table {table_number}")
    return orders

def calculate_bill(orders, table_number):
    t_str = str(table_number)
    if t_str not in orders:
        return 0, []
    
    subtotal = 0
    for item in orders[t_str]['items']:
        subtotal += item['price'] * item['quantity']
    
    return subtotal, orders[t_str]['items']

def close_order(orders, table_number):
    t_str = str(table_number)
    if t_str in orders:
        orders[t_str]['active'] = False
        del orders[t_str]
    return orders

