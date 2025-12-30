import os
import tables
import menu
import orders
import storage
import reports

DATA_DIR = 'data'

def main():
    t_data, m_data, o_data = storage.load_state(DATA_DIR)
    
    t_data = tables.initialize_tables(t_data)
    m_data = menu.initialize_menu(m_data)
    
    while True:
        print("\n=== Restaurant Management System ===")
        print("1. View/Manage Tables")
        print("2. Manage Orders")
        print("3. Manage Menu")
        print("4. Save & Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            tables.get_table_status(t_data)
            action = input("(S)eat Table, (R)elease Table, or (B)ack? ").lower()
            if action == 's':
                try:
                    t_num = int(input("Table Number: "))
                    p_size = int(input("Party Size: "))
                    srv = input("Server Name: ")
                    res = tables.assign_table(t_data, t_num, p_size, srv)
                    if res:
                        o_data = orders.open_order(o_data, t_num)
                        print("Table Seated.")
                except ValueError:
                    print("Invalid input.")
            elif action == 'r':
                try:
                    t_num = int(input("Table Number: "))
                    subtotal, items = orders.calculate_bill(o_data, t_num)
                    if subtotal > 0:
                        print(f"Table has an open bill of {subtotal} TL. Please close order first.")
                    else:
                        tables.release_table(t_data, t_num)
                        print("Table Released.")
                except ValueError:
                    print("Invalid input.")

        elif choice == '2':
            t_num = input("Enter Table Number: ")
            if not t_num.isdigit(): 
                continue
            t_num = int(t_num)
            
            print(f"\n--- Order for Table {t_num} ---")
            subtotal, items = orders.calculate_bill(o_data, t_num)
            for i in items:
                print(f"{i['quantity']}x {i['name']} - {i['price']*i['quantity']} TL")
            print(f"Total: {subtotal} TL")
            
            action = input("(A)dd Item, (P)rint Bill, (C)lose/Pay, (B)ack: ").lower()
            
            if action == 'a':
                menu.print_menu(m_data)
                iname = input("Item Name: ")
                try:
                    qty = int(input("Quantity: "))
                    o_data = orders.add_item_to_order(o_data, t_num, m_data, iname, qty)
                except ValueError:
                    print("Invalid quantity.")
            
            elif action == 'p':
                print(f"\nBILL FOR TABLE {t_num}")
                print("-" * 20)
                for i in items:
                    print(f"{i['name']}: {i['quantity']} x {i['price']} = {i['quantity']*i['price']}")
                print(f"TOTAL: {subtotal} TL")
                
            elif action == 'c':
                print(f"Final Total: {subtotal} TL")
                confirm = input("Confirm payment? (y/n): ")
                if confirm.lower() == 'y':
                    o_data = orders.close_order(o_data, t_num)
                    tables.release_table(t_data, t_num)
                    print("Order paid and table released.")

        elif choice == '3':
            menu.print_menu(m_data)
            action = input("(A)dd Item, (R)emove Item, (B)ack: ").lower()
            if action == 'a':
                name = input("Name: ")
                try:
                    price = float(input("Price: "))
                    cat = input("Category: ")
                    m_data = menu.add_menu_item(m_data, name, price, cat)
                except ValueError:
                    print("Invalid price.")
            elif action == 'r':
                name = input("Name to remove: ")
                m_data = menu.remove_menu_item(m_data, name)

        elif choice == '4':
            storage.save_state(DATA_DIR, t_data, m_data, o_data)
            print("Data saved. Exiting.")
            break

if __name__ == "__main__":
    main()
