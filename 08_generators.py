#
# GENERATORS (they act like ITERATORS)
#
#		def generator_name():
#			yield result
#
#	- structures that fetch values from a function
#	  and store them in iterables (lists, tuples, etc.)
#
#	- values are stored one by one, and each time a generator stores one,
#	  it maintains a suspended status until next value is requested
#
#	- more efficient than regular functions;
#	  specially useful with infinite values
#
print("----------------------- Pair numbers generator -----------------------")

def generate_pair_numbers(limit):
	num = 0
	pair_numbers = []
	while num < limit:
		pair_numbers.append(num * 2)
		num += 1
	return pair_numbers

print(generate_pair_numbers(10))
print()

def generate_pair_numbers_generator(limit):
	num = 0
	while num < limit:
		yield num * 2
		num += 1

pair_numbers_iterable = generate_pair_numbers_generator(10)
for pair_number in pair_numbers_iterable:
	print(pair_number, end=" ")
print('\n')

print("----------------------- Fibonacci numbers generator -----------------------")

def generate_fibonacci_numbers_generator_with_next():
	first, second = 0, 1
	while True:
		yield first
		first, second = second, first + second

fibo_numbers_iterable_next = generate_fibonacci_numbers_generator_with_next()
print("First ten Fibonacci numbers (starting in 0):")
for i in range(10):  # print ten first fibonacci numbers of an 'infinite' sequence
	print(next(fibo_numbers_iterable_next), end=", " if i != 9 else "")
print('\n')

print("----------------------- Cities generator -----------------------", end='')

def return_cities(*cities):
	#	for city in cities:
	#		for letter in city:
	#			yield letter
	for city in cities:  # the same as 3 lines above, but simplified
		yield from city  # return all letters as a continuous stream/flow

returned_city_letters = return_cities("Tokyo", "Amsterdam", "Sydney", "Los Angeles")
for city_letter in returned_city_letters:  # 65 to 91 is Unicode for A to Z
	print(('\n' if ord(city_letter) in list(range(65, 91)) else '') + city_letter, end='')
print()
