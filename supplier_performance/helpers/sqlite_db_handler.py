import sqlite3

# Create a connection to the SQLite database (it will create a new one if not exists)
conn = sqlite3.connect('synthetic_erp.db')

# Create a cursor object
cursor = conn.cursor()

# ----- Items ----- #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        commodity TEXT,
        criticality TEXT
    )
''')

# ----- Orders ----- #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        vendor TEXT NOT NULL,
        item_number INTEGER,
        quantity INTEGER,
        due_date DATETIME,
        item_costs FLOAT 
    )
''')

# ----- Receipts ----- #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS receipts (
        id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL,
        quantity_received INTEGER NOT NULL,
        received_date DATETIME
    )
''')

# ----- Inspection ----- #
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inspections (
        id INTEGER PRIMARY KEY,
        receipt_id INTEGER NOT NULL,
        inspection_date DATETIME
        quantity_inspected INTEGER NOT NULL,
        quantity_accepted INTEGER NOT NULL,
        quantity_rejected INTEGER NOT NULL,
        defect TEXT
    )
''')