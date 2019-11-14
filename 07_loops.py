import math

# Loop FOR - Syntax: 'for var in iterable: { loop body }'
# 	NOTE: iterables: lists, tuples, text (char array), ranges, etc.
print("----------------------- Simplest example -----------------------")
for i in [1, 2, 3]:  # executed once per element in the 'col'
    print("test")
print()

print("----------------------- Using the index -----------------------")
for word in ["first", "second", "third", "fourth", "fifth"]:
    print(word)  # using the index
print()

print("----------------------- Divide a word with symbols -----------------------")
word = "largeword"
counter = 0

for letter in word:
    print(letter, end="-" if counter != len(word) - 1 else "")
    counter += 1
print("\n")  # used with '\n' to compensate line just above

print("----------------------- Find a letter in a str [simplex] -----------------------")
print("es" in "test")
print()

print("----------------------- Find a letter in a str [complex] -----------------------")
email = input("Introduce your email, please: ")
for let in email:
    if let == "@":
        valid = True
        break  # go outside the loop, breaking the iteration
else:  # different of 'else' in IF sentence
    #	executed when the loop is empty (at any iteration point)
    valid = False
print(f"Valid email? {valid}")
print()

print("----------------------- Remove vowels -----------------------")
word_without_vowels = ""
for let_ in "complex_and_long_word":
    if let_ in ["a", "e", "i", "o", "u"]:
        continue  # skip current iteration, but continue the next
    else:
        word_without_vowels += let_
print(f"Result: {word_without_vowels}")
print()

print("----------------------- Pair numbers -----------------------")
for n in range(0, 10, 2):  # third param is the interval between values
    print(f"Number {n}")
print()

print("----------------------- Mail validator -----------------------")
email_1 = "email@domain.com"
email_2 = "aaggagdheje3jtm"
found_1 = False
found_2 = False
output = 'There was a problem'

for i in range(len(email_1)):  # iterates from 0 to (email_length - 1)
    if email_1[i] == "@":  # letter by letter
        output = "Valid email!"
        found_1 = True
    else:
        if not found_1:
            output = "Incorrect email!"
print(output)

for i in range(len(email_2)):
    if email_2[i] == "@":
        output = "Valid email!"
        found_2 = True
    else:
        if not found_2:
            output = "Incorrect email!"
print(output)
print()

# Loop WHILE - Syntax: 'while condition: { loop body }'
print("----------------------- Age validator -----------------------")
age = int(input("Introduce your age: "))

while not 0 < age < 100:
    print("Invalid age")
    age = int(input("Please, introduce your age: "))
print("Thanks for the info")
print()

print("----------------------- Square root calculator -----------------------")

num = int(input("Introduce a number with integer square root: "))

while math.modf(math.sqrt(num))[0] > 0:
    print("Invalid number")
    num = int(input("Introduce a number with an integer square root: "))
print(f"Square root of {num} is {math.sqrt(num)}")
