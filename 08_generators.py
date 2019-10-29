#
# GENERATORS (they act like ITERATORS)
#
#		def generator_name():
#			yield result
#
#	Structures that fetch values from a function and store them in iterables. Values are stored one by one,
#	and each time a generator stores one, it stops until next value is requested.
#
#	ADVANTAGES:	More efficient than regular functions, and specially useful with infinite collections, because of
#	their less memory usage and because they are "lazy" evaluated.
#	DRAWBACKS: Results are available just once, generator size is unknown and they can't be indexed.
#
from functools import wraps

print("----------------------- Pair numbers generator -----------------------")

def classic_approach(limit):
	num = 0
	pair_numbers = []
	while num < limit:
		pair_numbers.append(num * 2)
		num += 1
	return pair_numbers

print(f'\tClassic approach (collection): {classic_approach(10)}')

def generator_approach(limit):
	num = 0
	while num < limit:
		yield num * 2
		num += 1

pair_numbers_iterable = generator_approach(10)
print('\tGenerator approach: ', end='')
for pair_number in pair_numbers_iterable:
	print(pair_number, end=' ')
print('\n')

print("----------------------- Fibonacci numbers generator -----------------------")

def generate_fibonacci_numbers_generator_with_next():
	first, second = 0, 1
	while True:
		yield first
		first, second = second, first + second

fibo_numbers_iterable_next = generate_fibonacci_numbers_generator_with_next()
print('\tFirst ten Fibonacci numbers (starting in 0):\n\t\t', end='')
for i in range(10):  # print ten first fibonacci numbers of an 'infinite' sequence
	print(next(fibo_numbers_iterable_next), end=", " if i != 9 else "")
print('\n')

#
#	If the value returned by the generator is an iterable, we can YIELD FROM that value, returning each value
#	from the iterable. This way, we're flattening the original iterable and returning value per value.
#
print("----------------------- Cities generator -----------------------", end='')

def return_cities(*cities):
	#	for city in cities:
	#		for letter in city:
	#			yield letter
	for city in cities:  # the same as 3 lines above, but simplified
		yield from city  # return all letters as a continuous stream/flow

returned_city_letters = return_cities("Tokyo", "Amsterdam", "Sydney", "Los Angeles")
for city_letter in returned_city_letters:  # fetch all letters from all cities
	# 65 to 91 is Unicode for A to Z
	print(('\n\t' if ord(city_letter) in list(range(65, 91)) else ''), city_letter, sep='', end='')
print()

#
#	We can build COROUTINES using generators, allowing not only fetch values FROM the generator, but also send
#	values TO the generator. We can use it as a generator, using next() to obtain next value, or we can use
#	send() method to allow the generator to receive values.
#		- Due to the fact generators are lazy evaluated, it's mandatory to make a first next() call to active
#		the coroutine and be able to send it values.
#		- Once the coroutine is ACTIVE, we can send messages, or even throw exceptions TO the coroutine.
#		- Also, because we build them using infinite loops, we must remember to CLOSE no longer used coroutines.
#
print("\n----------------------- Spam generator -----------------------")

def coroutine(gen):
	@wraps(gen)
	def coroutine_(*args, **kwargs):
		active_coroutine = gen(*args, **kwargs)
		next(active_coroutine)
		return active_coroutine
	return coroutine_

@coroutine
def spam():
	print('\tSetting up generator...')
	try:
		while True:
			value = yield
			print(f'\t\tValue received -> {value}')
	except GeneratorExit:
		print('\tGenerator stopped.')
	except Exception as e:
		print(f'\tException caught: {e}')
	finally:
		print('\tExiting...')

corout = spam()
corout.send('one')
corout.send(2)
next(corout)  # if no value was previously send, it will return None
corout.send(3)
corout.send('four')
#corout.throw(RuntimeError, 'intentional error')
corout.close()

#
#	Coroutines can have a STATE and return values depending on that state.
#	We can also CHAIN coroutines, each one handling a different responsibility.
#
print("\n----------------------- Averager and chained average -----------------------")

@coroutine
def average():
	# first execution initializes 'count' = 1 and 'total' with first value sent;
	# first "send" will enter at first 'yield', and exit (and return) at second 'yield'
	count = 1
	total = yield
	while True:
		# when send() is called, the value provided is stored as: total = curr_total + yield (new value);
		# then, the loop continues, increasing the counter, and returning to 'yield' line, which will
		# current average as: new_total (+yield) / new_count (+1)
		total += yield total / count  # following values will enter and return at this line
		count += 1

averager = average()
print('\tElements: 1 | Value: 20  | Average: ' + str(averager.send(20)))
print('\tElements: 2 | Value: 10  | Average: ' + str(averager.send(10)))
print('\tElements: 3 | Value: 15  | Average: ' + str(averager.send(15)))
print('\tElements: 4 | Value: -25 | Average: ' + str(averager.send(-25)))
print()

@coroutine
def format_():
	while True:
		values_map = yield
		print(f'\tElements: {values_map["count"]} | Value: {values_map["value"]}  | Average: {values_map["average"]}')

@coroutine
def chained_average(target):
	count = 0
	total = 0
	while True:
		count += 1
		value = yield
		total += value
		target.send({'count': count, 'value': value, 'average': total / count})

formatter = format_()
chained_averager = chained_average(formatter)
chained_averager.send(20)
chained_averager.send(10)
chained_averager.send(15)
chained_averager.send(-25)
