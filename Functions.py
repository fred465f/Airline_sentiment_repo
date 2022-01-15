import sqlite3
import csv

# Query database and show result (advanced)
def query(name, sql):
	# Get cursor and connection
	c, conn = get_curser_connection(name)

	# Query database - rowid is made behind the scenes as a primary key
	c.execute(sql)
	all = c.fetchall()

	# Print query result
	for one in all:
		try:
			print(one)
		except:
			print("\n\nFail!\n\n")

	# Commit query and close connection
	commit_close(conn)

	# Return result
	return all

# Query database and show rows (simple)
def show(name, rows=5, columns="*", where=""):
	# Get cursor and connection
	c, conn = get_curser_connection(name)

	# Query database - rowid is made behind the scenes as a primary key
	c.execute(f"""
		SELECT rowid, {columns} FROM Tweets 
		{where}
		LIMIT {rows};""")
	all = c.fetchall()

	# Print query result
	for one in all:
		try:
			print(one)
		except:
			print("\n\nFail!\n\n")

	# Commit query and close connection
	commit_close(conn)

# Create/connect database name and get cursor
def get_curser_connection(name):
	# Create/connect database "customer.db"
	conn = sqlite3.connect(name)

	# Get cursor
	c = conn.cursor()

	# Return cursor
	return c, conn

# Commit changes to database and close connection
def commit_close(conn):
	# Commit changes to database
	conn.commit()

	# Close connection
	conn.close()

# Convert table to csv file
def table_to_csv(data, columns, filename='default.csv'):
	with open(filename, 'w', newline='') as f:
	    writer = csv.writer(f)
	    writer.writerow(columns)
	    writer.writerows(data)
	    print('File succesfully uploaded!')