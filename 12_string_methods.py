#
# STRING METHODS (str.method())
#
#	upper()
#		transforms all letters to upper case
#	lower()
#		transforms all letters to lower case
#	capitalize()
#		transforms first letter to upper case and others to lower case
#	count(substr)
#		returns number of times 'substring' appears on 'str'
#	
#	find(substr[, start, end])
#		returns the lowest index of the 'substr' if found
#		if not found, returns -1; differs from lists' index() method because
#		the second raises a ValueError exception, instead of return -1
#	isdigit()
#		returns True if all chars in 'str' are digits, False otherwise
#	isalnum()
#		returns True if all chars in 'str' are alphanumeric, False otherwise
#	isalpha()
#		returns True if all chars in 'str' are letters, False otherwise
#	
#	split([sep[,maxsplit]]) - (default = ' ') <- trimming whitespaces
#		returns a list of str using 'sep' as
#		delimiter, and 'maxsplit' as list maxsize
#	strip([chars]) - (default = ' ')
#		returns a copy of the string with both leading and trailing 'chars' removed
#	replace(old_str, new_str[, count])
#		returns a copy where all 'old' occurrences have been replaced with 'new' ones
#	rfind(subtr[, start, end])
#		returns the highest index of the 'substr' if found; otherwise returns -1
#
print("----------------------- upper | lower | capitalize | count ------------------------")

lore_upper_lower = 'lOrE iPsUm DoLoR sIt AmEt'
print(f"""
Original text: '{lore_upper_lower}'
	Upper text: '{lore_upper_lower.upper()}'
	Lower text: '{lore_upper_lower.lower()}'
	Capitalize text: '{lore_upper_lower.capitalize()}'
	Number of o's: {lore_upper_lower.lower().count("o")}""")
print()

print("-------------------- find | rfind | isdigit | isalum | isalpha --------------------")

lore_alpha = 'Lore ipsum dolor sit amet'
lore_alnum = '2Lore ipsum do3lor sit amet'
print(f"""
Original text (alpha): '{lore_alpha}'
	Index of first letter 'o': {lore_alpha.lower().find('o')}
	Index of last letter 'o': {lore_alpha.lower().rfind('o')}
	Is 'Lore' alphabetical?: {lore_alpha[0:4].isalpha()}
	Is the whole text alphabetical? {lore_alpha.isalpha()} (whitespaces)

Original text (alnum): '{lore_alnum}'
	Is first letter numerical?: {lore_alnum[0].isdigit()}
	Is '2Lore' alphanumerical?: {lore_alnum[0:5].isalnum()}
	Is '2Lore ' alphanumerical?: {lore_alnum[0:6].isalnum()}
	Is the whole text alphanumerical? {lore_alnum.isalnum()} (whitespaces)""")
print()

print("----------------------------- split | strip | replace -----------------------------")

lore = 'Lore ipsum dolor sit amet'
noisy = ',,,,,rrttgg.....banana....rrr'
spelling = 'A really vad sentence esample'
print(f"""
Original text: '{lore}'
	Text divided by whitespaces: {lore.split()}
	Text divided by letter 'e': {lore.split('e')}

Original text: '{noisy}'
	Text stripped by default: {noisy.strip()}
	Text stripped using ',.grt': {noisy.strip(',.grt')}

Original text: '{spelling}'
	Corrected text: {spelling.replace('v', 'b', 1).replace('es', 'ex')}""")
print()