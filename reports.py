def daily_sales_report(orders_history):
    total_rev = 0
    for order in orders_history:
        for item in order.get('items', []):
            total_rev += item['price'] * item['quantity']
    return total_rev
