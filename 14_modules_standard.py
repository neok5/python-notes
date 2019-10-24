#
# STANDARD MODULES
#
#   Module 'copy': useful to make copies of memory referenced variables of collections or objects.
#
#   Module 'doctest' / 'unittest': used for testing from two different approaches.
#
#   Module 'html' / 'xml' / 'json': allows to easy handle data structures in HTML/XML/JSON formats. Web development.
#
#   Module 'pickle': has needed functions to work with files and objects.
#
#   Module 're': using the special regex syntax, it can be used for checks and seeks over strings.
#
#   Module 'socket': focused on communications between different machines through several protocols. Client-server apps.
#
#   Module 'sqlite3': it allows to interact with SQLite databases (contained on a single file).
#
#   Module 'sys': gives information about SO environment, or even control it in some scenarios.
#
#   Module 'threading': enables processes' splitting in several sub-processes, thanks to different parallel threads.
#
#   Module 'tkinter': most widely used GUI library in Python.
#
#   Module 'collections': introduced to improve built-in collections' functionalities.
#       - class Counter. It's a subclass of dictionary object. Takes an iterable and returns a dict, where
#           each key is an element, and its value it's the number of times that element is in the collection.
#       - class defaultdic(type). Works exactly like a python dictionary, except for it does not throw KeyError
#           when you try to access a non-existent key. Instead, it initializes the key with the element
#           of the data 'type' passed as argument at the creation. The 'type' is used just for default values.
#       - class OrderedDict. It's a dictionary where keys maintain the order in which they were inserted,
#           which means if you change the value of a key later, it will not change the position of the key.
#           In Python 3.6+, standard 'dicts' are natural sorted (ordered by insertion) by default.
#       - namedtuple(). It's a simple tuple that has names for its values, as if it were a dict. A quick and
#           easy way to model basic tiny temporary classes with less code.
#
#   Module 'datetime': useful for dates and times handling.
#       - We can define a current datetime simply using the class 'datetime' inside the module 'datetime', and
#           calling its function now(), which returns a 'datetime' object. We can access its info through several
#           properties such as 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond' and 'tzinfo'.
#       - A datetime object behaves as a tuple, so we cannot set its fields directly doing 'dt.field = 2000';
#           we must use replace() method, reassigning datetime object to itself 'dt = dt.replace(field=value)',
#           because replace doesn't modify the original, just returns a modified copy.
#       - To set a timezone, we can use the module 'pytz' and its class 'timezone', build and object indicating
#           the timezone textually (for example: Europe/Madrid), and use the object as 'dt = tz_object.localize(dt)'.
#           Using 'pytz.all_timezones' we can see a list of all existing timezones.
#       - We can go to the past or the future using 'timedelta' class from 'pytz', building an object that
#           receives as params several modifiable fields to calculate with, being the default one 'days'.
#           Later on, we can use that 'timedelta' object to sum or subtract it from any 'dt'.
#
#   Module 'math': includes a lot of mathematical functions to work and operate with.
#
#   Module 'random': useful for generate random content. Video-game development or test cases are good scenarios.
#
from collections import Counter, defaultdict, OrderedDict, namedtuple
from datetime import datetime as dt, timedelta as td
from pytz import timezone as tz

print("----------------------- Collections ------------------------")

animals = 'cat dog cat dolphin cat python dog hamster cat hamster tree dog'
counter = Counter(animals.split(' '))  # builds a Counter using words in the string
print(f'\t{counter}')
print(f'\tMost common animal -> {counter.most_common(1)[0][0]}')  # returns single most common animal
print(f'\tTwo most common animals -> {counter.most_common(2)[0][0]}, {counter.most_common(2)[1][0]}')
print()

def_dict = defaultdict(float)
print(f'\tInitial default dictionary: {def_dict}')
print(f'\tNot existing key \'fake_key\': {def_dict["fake_key"]}')
print(f'\tDefault dictionary after one access: {def_dict}')
print()

unord_dict_1 = {1: 'one', 2: 'two'}
unord_dict_2 = {2: 'two', 1: 'one'}
ord_dict_1 = OrderedDict({1: 'one', 2: 'two'})
ord_dict_2 = OrderedDict({2: 'two', 1: 'one'})
print(f'\tIs first unorder dict equals to second? {unord_dict_1 == unord_dict_2}')  # true; order doesn't matter
print(f'\tIs first order dict equals to second? {ord_dict_1 == ord_dict_2}')  # false; order matters and differs
print()

Person = namedtuple('Person', 'name lastname age')
john = Person(name='John', lastname='Wick', age=42)
print(f'\tName tuple Person \'jonh\' -> {john}')
print(f'\t{john.name}\'s age: {john.age}')
print()

print("----------------------- Datetime ------------------------")

ct = dt.now()
ct = tz('Europe/Madrid').localize(ct.replace(tzinfo=None))
print(f'\tCurrent datetime with Spain timezone: {ct}')
print(f'\tOther format: {ct.year}-{ct.month}-{ct.day} {ct.hour}:{ct.minute}:{ct.second}.{ct.microsecond} {ct.tzinfo}')

fakebday = dt(1992, 5, 23)
fakebday = fakebday.replace(year=1996)
print(f'\tBirthday + 4 years: {fakebday}')
days = td(days=5*365/12)
print(f'\tFive months ago in Tokyo: {dt.now(tz("Asia/Tokyo")) - days}')  # pytz is fully compatible with datetime module
