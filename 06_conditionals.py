#
# sentence IF
#
print("--- Exam evaluation ---")
# function that allows the user to introduce data using the keyboard
# any value introduced is a 'str'; it may be needed to convert it
user_mark = input("Insert your mark: ")


def evaluation(mark):
    resolution = "pass"
    if mark < 5:
        resolution = "fail"
    return resolution


print(evaluation(int(user_mark)))
print()

#
# sentence IF-ELIF-ELSE
#
print("--- Age verification ---")

user_age = int(input("Insert your age: "))


def verification(age_):
    if age_ < 18:
        print("Denied")
    elif age_ > 100:
        print("Incorrect")
    else:
        print("Allowed")


verification(user_age)
print()

#
# sentence IF concatenating arithmetic comparators
#
print("--- Age verification simplified ---")
age = int(input("Insert an age: "))

# it evaluates the condition from left to right, pair by pair
# same as: (age > 0) AND (age < 100) # params just for legibility
if 0 < age < 100:
    print("Valid age")
else:  # instructions outside a function; LOL
    print("Incorrect age")
print()

print("--- Employee salary evaluation ---")
ceo_salary = int(input("Introduce CEO`s salary: "))
print("CEO`s salary -> " + str(ceo_salary) + " $/year\n")
director_salary = int(input("Introduce director`s salary: "))
print("Director`s salary -> " + str(director_salary) + " $/year\n")
boss_area_salary = int(input("Introduce boss area`s salary: "))
print("Boss area`s salary -> " + str(boss_area_salary) + " $/year\n")
junior_salary = int(input("Introduce junior`s salary: "))
print("Junior`s salary -> " + str(junior_salary) + " $/year\n")

if ceo_salary > director_salary > boss_area_salary > junior_salary:
    print("Everything`s fine")
else:
    print("Something`s wrong")
print()

#
# sentence IF concatenating generic conditions (and, or)
#
print("--- Study grant validation ---")

distance = int(input("Insert the distance in kms: "))
siblings = int(input("Insert the number of brothers or sisters: "))
family_salary = int(input("Insert the annual salary of your family unit: "))

if distance > 40 and siblings > 2 or family_salary <= 20000:
    print("You have been granted your study grant")
else:
    print("You can`t access to this subvention")
print()

#
# sentence IF concatenating general conditions (w/ and, or, not)
#
print('--- Optional subjects ---')
print('Graphic computing | Software testing | Usability and accessibility')
subject = input("Select a subject: ").lower()

if subject in ("graphic computing", "software testing", "Usability and accessibility"):
    print("Selected subject: " + subject[0].upper() + subject[1:])
else:
    print("Selected subject doesn`t exists")
