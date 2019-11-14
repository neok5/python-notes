#
# EXCEPTIONS
#	
#	Error trace example:
#
#		Traceback (most recent call last):
#  			File "line_file_error___absolute_route", line 13, in <module>
#    			divide_by_zero()
#  			File "line_file_error___absolute_route", line 11, in divide_by_zero
#    			print(8/0)
#		ZeroDivisionError: division by zero
#
#	Handling exceptions:
#
#		* Syntax:
#			try:
#				sentence_raising_error
#				(... more sentences which raise errors ...)
#			except CaughtException: -> code executed when there's an error
#				code_to_handle_error
#			(... more caught exceptions and their handlers...)
#			else:  -> code executed when there's NO error
#				code_to_handle_success
#			finally:
#				when_error_is_raised_,_this_code_always_get_executed
#
#		* Sentence 'except' particularities:
#			# this captures any error, not recommended
#			except:
#			# this gives the exception an alias,
#			# and allows to handle several
#			except (ExceptionOne, ExceptionTwo,...) as e:
#
#	Rising exceptions:
#
#		* Syntax:
#			raise ErrorRaised("optional_custom_error_message")
#
#		* It can be raised: pre-built errors, user defined errors

print("----------------------- Calculator -----------------------")

def _sum(num_1, num_2):
	return num_1 + num_2

def subtract(num_1, num_2):
	return num_1 - num_2

def multiply(num_1, num_2):
	return num_1 * num_2

def divide(num_1, num_2):
	return num_1 / num_2

switcher = {  # there're no function calls, it only stores function declarations
	"sum": _sum,
	"subtract": subtract,
	"multiply": multiply,
	"divide": divide
}

operand_1 = int(input("Please, introduce the first operand: "))
operand_2 = int(input("Please, introduce the second operand: "))
operation = input("Introduce the op [sum, subtract, multiply, divide]: ")

correct_operation = False
while not correct_operation:
	# and here, the specific declaration is used to make a function call over it
	try:
		print(f"The result of the {operation} is {switcher.get(operation, 'Incorrect operation!')(operand_1, operand_2)}")
		correct_operation = True
		break  # breaks the infinite loop if there's no error
	except TypeError as e:  # otherwise, it keeps asking for a correct operation
		print(f"The operation '{operation}' DOES NOT exist")
		operation = input("Introduce the op [sum, subtract, multiply, divide]: ")
	finally:
		if correct_operation:
			print("Calculation ended")
print()

print("----------------------- Age evaluator -----------------------")

def eval_age(age):
	if age < 0:
		raise ValueError(f"\tException: age provided ({age}) is wrong; can't be negative")
	elif age < 18:
		print("You are underage")
		return False
	else:
		print("You are an adult")
		return True

try:
	# two sentences here can raise a ValueError:
	#	- a 'str' - invalid literal for int()
	#	- a negative number - error is raised in 'eval_age' function (l:84)
	age_result = eval_age(int(input("Please, introduce your age: ")))
except ValueError as ve:
	print(ve)
else:  # with a finally this would raise a NameError: name 'age_result' is not defined
	print(f'Age evaluator finished, you {"CAN" if age_result else "CANNOT"} pass')
