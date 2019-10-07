#
# CRUD APPLICATION
#
#	- Example of simple application that allows four basic operations in any database,
#	  known as CRUD: create, read, update and delete. The main entity will be an user,
#	  that stores some common information.
#
#	- We're gonna use four CRUD operations, as well as parameterized SQL queries
#	  Example: "curs.execute(f'INSERT INTO USER_DATA VALUES (NULL, ?, ?, ?, ?, ?)', user)"

# ----------------------- # APPLICATION # ----------------------- #
import api.api_crud_app as api

print("----------------------- Users CRUD application ------------------------")
users = [('username_1', 'surname_1', 'encoded_pass_1', 'address_1', 'remarks_1'),
	('username_2', 'surname_2', 'encoded_pass_2', 'address_2', 'remarks_2'),
	('username_3', 'surname_3', 'encoded_pass_3', 'address_3', 'remarks_3'),
	('username_4', 'surname_4', 'encoded_pass_4', 'address_4', 'remarks_4')]

print('Connecting (or creating) database...\n')
api.connect_db()

api.show_db()

print('\tAdding a few users...\n')
for user in users:
	api.create_user(user)
api.show_db()

print('\tUpdating second user as 23rd user...')
second_user = api.read_user(2)
print(f'\t\t{second_user}\n\t\t\tto')
second_user = (second_user[0], second_user[1] + '3', \
	second_user[2] + '3', second_user[3] + '3', second_user[4] + '3', second_user[5] + '3')
print(f'\t\t{second_user}\n')
api.update_user(second_user)
api.show_db()

print('\tDeleting third user...\n')
api.delete_user(3)
api.show_db()

print('Closing database connection...\n')
print('Exiting application...\n')
api.exit_app()