import sqlite3

# Connect to (or create) database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
);
""")

# Insert sample data
sample_data = [
    ("Laptop", 5, 70000),
    ("Laptop", 2, 72000),
    ("Mobile", 10, 15000),
    ("Mobile", 7, 16000),
    ("Tablet", 4, 25000),
    ("Tablet", 3, 24000),
    ("Headphones", 15, 2000),
    ("Headphones", 10, 2200),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("✅ sales_data.db created successfully with sample data!")
