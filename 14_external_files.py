#
# EXTERNAL FILES
#
#	- To handle external files, we have to use built-in Python module 'io'.
#	- To store information, there are 4 steps: creation, opening, handling and closing.
#
#	- Module 'io' utilities:
#		· open(file[, mode[, encoding]]) - open the specified file
#			file: path-like object representing a file system path
#			encoding: specifies the encoding to use (recommended: 'UTF-8')
#			mode:
#				'r'	- reading | (default)
#				'w'	- writing | creates a new file, or truncates it if already exists
#				'a'	- appending | creates a new file, or add content at the end
#								  without truncating it if it already exists
# 				't'	- text mode (default)
#				'b'	- binary mode
#				'+'	- updating (reading and writing)
#		· read([n_chars]) - read atmost 'n_chars' from file, or till end if not specified
#						  	reads the file, but also sets the pointer to last char read
#		· readline([n_chars]) - read and return one line from file
#		· readlines([n_chars]) - read an return a list of lines from file
#		· write(str) - write the str to the file and return number of chars written
#		· writelines([str_1, str_2, ...]) - write a list of lines to file
#		· close() - close an opened file (has no effects if the file is already closed)
#		· seek(pointer_index) - set file pointer to specified index (starting from 0)
#
import io
filename = '14_text_file.txt'
print("----------------------- External files handling ------------------------")

def remove_last_char(text): # function to map to each element
	return text[0:len(text)-1] # removes last character

file_write = open(filename, 'w') # opened in write mode (creates or truncates the file)
text = "Line 1\nLine 2\nLine 3\n"
# opening files in text mode (default) creates a '_io.TextIOWrapper'
print(f'{type(file_write)}')
print(f"Writing next content to file:\n{text}")
file_write.write(text)
file_write.close()
del file_write

file_read = open(filename, 'r')
print(f"Reading whole file content:\n{file_read.read()}")
file_read.close() # we need to open it two times to do two readings
del file_read

file_read_lines = open(filename, 'r')
print(f"Reading file line by line:")
print(*map(remove_last_char, file_read_lines.readlines()), sep = ' | ')
file_read_lines.close()
del file_read_lines
print()

file_append = open(filename, 'a+') # append reading and writing from end position
new_line = 'Line 4\n'
print(f"Appending one line to file:\n{new_line}")
file_append.write(new_line)
file_append.close()
del file_append

print("----------------------- Pointers over text files ------------------------")

file_middle = open(filename, 'r')
file_size = int(len(file_middle.read()))

file_middle.seek(file_size/2) # sets the pointer in the middle of the file
print(f"Reading from middle to end:{file_middle.read()}") # middle to end

file_middle.seek(0) # restarts the pointer after second read; from start to middle
print(f"Reading from start to middle:\n{file_middle.read(int(file_size/2))}")

file_middle.seek(0) # restarts the pointer after second read
file_middle.seek(len(file_middle.readline())) # sets the pointer at first line's end
print(f"Reading from second line to end: {file_middle.read()}", end = '')
file_middle.close()
del file_middle
print()

print("----------------------- Editing text file lines ------------------------")

file = open(filename, 'r+') # read and write mode
file_lines = file.readlines()
second_line = file_lines[1] # second line is cached
penultimate = len(second_line) - 1 # second line's penultimate char pointer is cached
print(f"""File lines:
	{file_lines}
""")

second_line_pref = f"{second_line[0:penultimate]}" # line feed prefix
second_line_suff = f"{second_line[penultimate:penultimate+1]}" # line feed suffix
file_lines[1] = f"{second_line_pref}3{second_line_suff}" # inserts a '3' between both
print(f"""Modified file lines:
	{file_lines}""")
file.seek(0) # moves the pointer from the end to the beginning
file.writelines(file_lines)
file.close()
del file
print()