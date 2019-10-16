#
# PERMANENT STORAGE
#
#	- Sometimes you can have certain information you don't want to lose,
#	  and even you want to use it regardless with different applications.
#	  That's the concept of permanent storage (in a file, a database, etc.).
#
from pickle import dump, load

class Person:

	def __init__(self, name, genre, age):
		self.name = name
		self.genre = genre
		self.age = age
		print(f'A new person was created: "{self.name}"')

	def __str__(self):
		return f'{self.name} {self.genre} {self.age}'

class PeopleList:

	people = []
	filename = '17_peoplelist_permstorage'

	def __init__(self):
		people_file = open(self.filename, 'ab+') # append (end of file), read-write and binary
		people_file.seek(0) # set the pointer at start to read the file

		try:
			self.people = load(people_file) # read and loads the file
			print(f'{len(self.people)} people were loaded from external file')
		except EOFError:
			# if file is empty it will raise a EOFError
			print('File is empty')
		finally:
			people_file.close()
			del people_file

	def add_people(self, people_list):
		for person in people_list:
			self.people.append(person)
		self.__save_people_perm_storage()

	def show_people(self):
		print('External file information is:')
		for person in self.people:
			print(f'\t{person}')

	def __save_people_perm_storage(self):
		people_file = open(self.filename, 'wb') # write binary mode; truncates files echa time
		dump(self.people, people_file)
		people_file.close()
		del people_file

print("----------------------- People list ------------------------")

my_people = PeopleList() # comment below line to avoid constantly write on the file
my_people.add_people([Person('Albert', 'Male', 27), Person('Marie', 'Female', 32)])
print()
my_people.show_people()
print()