# ----------------------- # API # ----------------------- #
import sqlite3 as db
import os # to delete the db each time

db_name = '18_crud_app_users_db'
if os.path.isfile(db_name):
	os.remove(db_name) # this allows to start from scratch each time
# global 'conn' and 'curs' access
conn = db.connect(db_name)
curs = conn.cursor()

def connect_db():
	try:
		curs.execute('''CREATE TABLE USER_DATA (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			USERNAME VARCHAR(40),
			SURNAME VARCHAR(40),
			PASS VARCHAR(20),
			ADDRESS VARCHAR(70),
			REMARKS VARCHAR(200))''')

		conn.commit()
	except:
		pass

def create_user(user):
#	curs.execute(f"""INSERT INTO USER_DATA VALUES
#		(NULL, '{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}', '{user[4]}')""")

	# alternatively, we can do a parameterized SQL query
	curs.execute(f'INSERT INTO USER_DATA VALUES (NULL, ?, ?, ?, ?, ?)', user)
	conn.commit()

def read_user(user_id):
	curs.execute(f'''SELECT * FROM USER_DATA WHERE ID = {user_id}''')
	return curs.fetchone()

def update_user(user):
	curs.execute(f"""UPDATE USER_DATA
		SET USERNAME = '{user[1]}', SURNAME = '{user[2]}', PASS = '{user[3]}',
			ADDRESS = '{user[4]}', REMARKS = '{user[5]}'
		WHERE ID = {user[0]}""")
	conn.commit()

def delete_user(user_id):
	curs.execute(f"""DELETE FROM USER_DATA WHERE ID = {user_id}""")
	conn.commit()

def close_db():
	conn.close()

def exit_app():
	# exists any Python script; in console, quit() or exit() are preferable
	raise SystemExit()

# ----------------------- # UTILS # ----------------------- #

def count_users():
	curs.execute('SELECT COUNT(*) FROM USER_DATA')
	return curs.fetchone()[0] # return an element instead of a list

def max_id():
	curs.execute('SELECT MAX(ID) FROM USER_DATA')
	max_id = curs.fetchone()[0]
	return max_id if max_id is not None else 0

def show_db():
	print(f'\tShowing database ({count_users()} users):')
	print('\t\tID, USERNAME, SURNAME, PASS, ADDRESS, REMARKS')

	for user_id in range(1, max_id()+1):
		user_db = {read_user(user_id)}
		if user_db != {None}:
			print(f'''\t\t{user_db}''')
	print()