def initialize_tables(existing_tables=None):
    if existing_tables:
        return existing_tables
    
    tables = []
    t_id = 1
    
    for _ in range(4):
        tables.append({'id': t_id, 'capacity': 4, 'status': 'free', 'server': None})
        t_id += 1
        
    for _ in range(2):
        tables.append({'id': t_id, 'capacity': 2, 'status': 'free', 'server': None})
        t_id += 1
        
    for _ in range(4):
        tables.append({'id': t_id, 'capacity': 8, 'status': 'free', 'server': None})
        t_id += 1
        
    return tables

def assign_table(tables, table_number, party_size, server_name):
    for t in tables:
        if t['id'] == table_number:
            if t['status'] != 'free':
                print(f"Table {table_number} is already occupied.")
                return None
            if party_size > t['capacity']:
                print(f"Party size {party_size} exceeds capacity {t['capacity']}.")
                return None
            
            t['status'] = 'occupied'
            t['server'] = server_name
            return t
    print(f"Table {table_number} not found.")
    return None

def release_table(tables, table_number):
    for t in tables:
        if t['id'] == table_number:
            t['status'] = 'free'
            t['server'] = None
            return True
    return False

def get_table_status(tables):
    print(f"{'ID':<5} {'Cap':<5} {'Status':<10} {'Server'}")
    print("-" * 35)
    for t in tables:
        srv = t['server'] if t['server'] else "N/A"
        print(f"{t['id']:<5} {t['capacity']:<5} {t['status']:<10} {srv}")
