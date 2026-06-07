import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Delete old tables if they exist
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS orders")

# Create Users Table
cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT,
    role TEXT
)
""")

# Create Products Table
cursor.execute("""
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    price REAL,
    description TEXT
)
""")

# Create Orders Table
cursor.execute("""
CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER,
    status TEXT
)
""")

# Insert Products
products = [
    ('Laptop', 55000, 'High Performance Laptop'),
    ('Smartphone', 25000, 'Android Smartphone'),
    ('Headphones', 3000, 'Wireless Bluetooth Headphones'),
    ('Smart Watch', 5000, 'Fitness Smart Watch'),
    ('Tablet', 18000, 'Android Tablet'),
    ('Camera', 35000, 'Digital Camera'),
    ('Sports Shoes', 2499, 'Running Shoes'),
    ('Backpack', 999, 'Travel Backpack')
]

cursor.executemany(
    "INSERT INTO products(product_name, price, description) VALUES (?, ?, ?)",
    products
)

conn.commit()
conn.close()

print("Database Created Successfully!")
