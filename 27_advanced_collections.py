#
# ADVANCED COLLECTIONS
#
#   - ChainMap. Allows to join several dictionaries and access to any of internal mappings of any of the dictionaries
#               as if they were all of them a single dictionary. It does NOT create more objects in memory, Python
#               just assumes that role and link them together virtually.
#
#   - Deque. Double ended queue; it's a double linked list, where each element is linked with its previous and next
#            element, so the list itself only has pointers for first and last elements. This performs a O(1) complexity
#            in accessing or removing elements from the 'deque'.
#
#   - Heapd. It makes easier building priority queues. Internally, it's a binary tree where each parent node has
#            a value less or equal to any of each children. Example ([] - children):
#                                                           1[2[7[], 3[]], 3[4[], 5[]]]
#
#   - Bisect. It's a kind of list that inserts all its elements so they are always sorted. Bisect insertion is
#             a O(n) operation, so create a list of n elements could have a O(n^2) complexity.
#
#   - Enum. Useful for constants arrangement in modules.
#
import collections as col
import heapq
import bisect
import enum

fullname = {
    'name': 'John',
    'lastname': 'Wick'
}

address = {
    'street': 'Fake',
    'streetnum': 555,
    'city': 'Ohio',
    'postcode': 12345
}

class Color(enum.Enum):
    red = '#FF0000'
    blue = '#0000FF'
    aquamarine = '#7FFFD4'

user = col.ChainMap(fullname, address)
print(f'''
    Fullname: {user.get("name")} {user.get("lastname")}
    Address: {user.get("street")} street, nº{user.get("streetnum")}
             {user.get("city")}, {user.get("postcode")}
''')

print('· Initial queue...')
queue = col.deque()
print(f'\t{queue}\n')

print('· Adding elements to the right...')
queue.append('one')
queue.append(2)
print(f'\t{queue}\n')

print('· Adding elements to the left')
queue.appendleft('zero')
queue.appendleft(-1)
print(f'\t{queue}\n')

print('· Removing elements from the right')
queue.pop()
print(f'\t{queue}\n')

print('· Removing elements from the left')
queue.popleft()
print(f'\t{queue}\n')

circular_queue = col.deque(maxlen=3)
for n in range(1, 6):
    circular_queue.append(n)  # appends right and removes (automatically) left
    print(f'\t{circular_queue}')
print()

reverse_circular_queue = col.deque(maxlen=3)
for n in range(1, 6):
    reverse_circular_queue.appendleft(n)  # appends left and removes (automatically) right
    print(f'\t{reverse_circular_queue}')
print()

heap = [1, 2, 3, 4, 5]
heapq.heapify(heap)  # this does NOT create a new list, just change its order
print(f'\tInitial heap: {heap}')

print(f'\tPop {heapq.heappop(heap)} -> {heap}')
print(f'\tPop {heapq.heappop(heap)} -> {heap}')
print(f'\tPop {heapq.heappop(heap)} -> {heap}')
print(f'\tPop {heapq.heappop(heap)} -> {heap}')
print(f'\tPop {heapq.heappop(heap)} -> {heap}')

heapq.heappush(heap, 5)
print(f'\tAdd 1 -> {heap}')
heapq.heappush(heap, 4)
print(f'\tAdd 2 -> {heap}')
heapq.heappush(heap, 3)
print(f'\tAdd 3 -> {heap}')
heapq.heappush(heap, 2)
print(f'\tAdd 4 -> {heap}')
heapq.heappush(heap, 1)
print(f'\tAdd 5 -> {heap}')
print()

sorted_list = []
bisect.insort_right(sorted_list, 40)
bisect.insort_right(sorted_list, 7)
bisect.insort_right(sorted_list, -1)
bisect.insort_right(sorted_list, 23)
bisect.insort_right(sorted_list, 2)
bisect.insort_right(sorted_list, 200)
bisect.insort_right(sorted_list, 0)
print(f'\tSorted list: {sorted_list}')
print()

# we can access through dot notation, [key] or (value)
print(f'\tColor aquamarine -> {Color.aquamarine} | {Color["aquamarine"]} | {Color("#7FFFD4")}')
print(f'\tAquamarine name = \'{Color.aquamarine.name}\' | Aquamarine value = {Color.aquamarine.value}')
print(f'\tIs {Color.red} equals to {Color("#FF0000")}? {Color.red is Color("#FF0000")}')
