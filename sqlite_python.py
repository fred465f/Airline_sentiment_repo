import sqlite3

# Create database, do stuff to it, and terminate it when program ends
# conn = sqlite3.connect(":memory:")

# Create/connect database "customer.db"
conn = sqlite3.connect("customer.db")

# Get cursor
c = conn.cursor()

# Create a table
c.execute("""
CREATE TABLE customers (
	first_name TEXT,
	last_name TEXT,
	email TEXT
);
	""")

# Insert a row
c.execute("""
INSERT INTO customers VALUES (
	'Frederik',
	'Rytter',
	'jessheimfred@gmail.com'
);
	""")

# Insert rows
items = [('Frederik', 'Rytter', 'jessheimfred@gmail.com'),
('Frederik', 'Rytter', 'jessheimfred@gmail.com'),
('Frederik', 'Rytter', 'jessheimfred@gmail.com')]

c.executemany("""
INSERT INTO customers VALUES (?,?,?);
	""", items)

# Query database - rowid is made behind the scenes as a primary key
c.execute("SELECT rowid, * FROM customers")
# c.fetchone()
# c.fetchmany(2)
all = c.fetchall()
for one in all:
	print(one)

# Commit changes to database
conn.commit()

# Close connection
conn.close()

print("Commit done!")