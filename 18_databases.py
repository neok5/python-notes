#
# DATABASES
#
#	- Python supports several DBMS, both SQL (Oracle, SQLite...) and noSQL (MongoDB, Redis...)
#
#	- SQLite: DBMS SQL, written in C, open source, integral part of the program it belongs:
#		stored in a single file. Benefits: lightweight, efficient and fast, multi-platform,
#		no requires management/configuration. Drawbacks: doesn't allow nested clauses (where),
#		it has no users (single access at the same time).
#
#	- General steps to connect to SQL databases:
#		· open-create connection
#			· create cursor (pointer)
#				· execute query SQL
#				· handle query results (CRUD)
#			· close cursor (pointer)
#		· close connection
#
import sqlite3 as db
import os  # to delete the db each time

db_name = '18_products_sqlite_db'

def show_list(_cursor):
	_cursor.execute('SELECT * FROM PRODUCTS')
	elements_list = _cursor.fetchall()
	
	print('\t\tAll products:')
	for element in elements_list:
		print(f'\t\t\t{element}')
	print()

print("----------------------- SQLite database ------------------------")

print('Removing db (if exists)')
if os.path.isfile(db_name):
	os.remove(db_name)

print('Opening/creating connection...')
connection = db.connect(db_name)

print('\tCreating cursor...')
cursor = connection.cursor()

# due to this table has a primary key field, if we try to insert two records
# 	(at the same time, or sequently) with the exact same primary key (KEY),
# 	will raise a 'sqlite3.IntegrityError: Unique constraint failed: [name_of_the_field]'
# it can't have neither two records with same PRODUCT_CODE (UNIQUE field: IntegrityError)
cursor.execute("""CREATE TABLE PRODUCTS (KEY INTEGER PRIMARY KEY AUTOINCREMENT,
	PRODUCT_CODE VARCHAR(4) UNIQUE, NAME VARCHAR(50), QUANTITY INTEGER, SECTION VARCHAR(20))""")

print('\t\tExecuting SQL query...', end='\n\n')

# we have to set first field to NULL, so as to Python treat it as self-increasing
cursor.execute('''INSERT INTO PRODUCTS VALUES
	(NULL, "PR01", "Adidas blue t-shirt", 500, "Sport clot.")''')

# inserting several records at the same time
products = [
	('PR02', 'Apple Macbook Air', 70, 'Technology'),
	('PR03', 'Nike red shoes', 200, 'Sport clot.'),
	('PR04', 'Nesquick 400 gr', 2300, 'Food')
]
# as many question marks as fields the record to insert has (including NULL primary key)
cursor.executemany('INSERT INTO PRODUCTS VALUES(NULL, ?, ?, ?, ?)', products)

show_list(cursor)

cursor.execute('SELECT * FROM PRODUCTS WHERE SECTION LIKE "Sport clot."')
sport_products_db = cursor.fetchall()
# we can user fetchone() here, to get only one element of the returned list
print('\t\tSport clothes:')
for sport_prod in sport_products_db:
	print(f'\t\t\t{sport_prod}')
print()

print('\t\tUpdating second product QUANTITY...')
cursor.execute('UPDATE PRODUCTS SET QUANTITY = 120 WHERE KEY = 2')
show_list(cursor)

print('\t\tDeleting third product...')
cursor.execute('DELETE FROM PRODUCTS WHERE KEY = 3')
show_list(cursor)

print('\t\tHandling query results...')

print('\tCommitting changes...')
connection.commit()

print('Closing connection...')
connection.close()
print()
