#
# SCRIPTS
#
#	- A 'script' is a set of instructions in source code which executes from top to bottom, sequentially.
#		It's saved in a single file with a unique name and executed from the interpreter. It can receive
#		several arguments when it's called or executed.
#
#	- To enable script arguments catch, we must import 'sys' built-in Python library. We can then access to
#		'argv' (sys.argv | non-named arguments) to obtain a list of arguments gave in script call.
#		It'a a good practice to check arguments integrity before script code.
#
#	- Arguments are passed always as strings, and the first argument will be script name, beginning actual
#		arguments after that. So even a script execution with no params, will have at least 1 argument (argv[0]).
#		The script name will have the complete absolute path for the script in the system.
#
import sys
print("---------------------- Taking params from commandline -----------------------\n")

def indent_text(_text, _reps):
	"""expects 2 arguments: the \'text\' and the number of \'reps\'"""
	tab = ['\t']
	for i in range(_reps):
		print(f'{"".join(tab*i)}{_text}')

if len(sys.argv) == 3:
	text = sys.argv[1]
	reps = int(sys.argv[2])
	indent_text(text, reps)
else:
	print('There was an error, see help below...')
	help(indent_text)
