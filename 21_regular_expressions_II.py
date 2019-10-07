#
# REGULAR EXPRESSIONS (II)
#
#	- A range is a special case of 'character set' where you can specify a range of
#	 characters (letters) or a range of digits (numbers). Even you can use an anchor
#	 to search for a range of elements at the beginning or at the end of a string.
#
#		· It's case sensitive, so it's not the same '[a-z]' that '[A-Z]'
#
#	- Common useful metacharacters:
#
#		'[]' a set of characters
#
#		'.' any character except new line ones ('\n', '\r')
#
#		'{n}' exactly n occurrences of preceding element
#
#		'{n,}' at least n occurrences of preceding element
#
#		'{m, m}' at least n and at most m occurrences of preceding element
#
#		'|' either or (or one or the other)
#
#		'()' capture and group
#
#	- Common useful special sequences:
#	 (has been used "The rain in Spain" as example)
#
#		'\A' specified chars at start of the string
#		'\Z' specified chars at end of the string
#			· '\AThe' finds ['The']
#			· 'Spain\Z' finds ['Spain']
#
#		'\b' specified chars at start or end of a word, acts like a word boundary (delimiter)
#		'\B' specified chars NOT at start or end of a word, acts like the inverse of '\b'
#			· '\bain' finds [] - occurrences of 'ain' at the beginning
#			· 'ain\B' finds [] - occurrences of 'ain' NOT at the end
#			· '\Bain' finds ['ain', 'ain'] - occurrences of 'ain' NOT at the beginning
#			· 'ain\b' finds ['ain', 'ain'] - occurrences of 'ain' at the end
#
#		'\d' DOES contain digits
#		'\D' DOES NOT contain digits
#			· '\d' finds []
#			· '\D' finds ['T','h','e',' ','r','a','i','n',' ','i','n',' ','S','p','a','i','n']
#
#		'\s' DOES contain a white space character (returns whitespaces)
#		'\S' DOES NOT contain a white space character (returns any but whitespaces)
#			· '\s' find [' ',' ',' ']
#			· '\S' finds ['T','h','e','r','a','i','n','i','n','S','p','a','i','n']
#
#		'\w' DOES contain any word characters ([a-Z] or [0-9] or [_] underscore)
#		'\W' DOES NOT contain any word characters
#			· '\w' find ['T','h','e','r','a','i','n','i','n','S','p','a','i','n']
#			· '\W' finds [' ',' ',' ']
#
import re

names = ['Albert', 'Nikola', 'Marie', 'Isaac', 'Leonardo', ''] # empty name at the end

def show_parsed_names(pattern):
	for name in names:
		if re.search(pattern, name, re.I):
			print(f'\n\t\t· {name}', end = '')
	print('\n')

print(f'\tNames:')
show_parsed_names('')

print("----------------------- Parsing names (normal) ------------------------\n")

print(f'\tNames starting with a letter from \'A\' to \'L\':')
show_parsed_names('^[A-L]')

print(f'\tNames ending with a letter from \'C\' to \'O\':')
show_parsed_names('[C-O]$')

print(f'\tNames containing a letter from \'I\' to \'K\':')
show_parsed_names('[I-K]')

print(f'\tNames containing a letter from \'J\' to \'K\':')
show_parsed_names('[J-K]')

print("----------------------- Parsing names (negate) ------------------------\n")

print(f'\tNames without vowels \'E\' or \'O\':')
# start line | (any symbol except E or O) 0 or more times | end line
show_parsed_names('^((?![EO]).)*$')

print(f'\tNames without vowels \'I\':')
show_parsed_names('^((?![I]).)*$')

print(f'\tNames without letters \'B\' or \'C\':')
show_parsed_names('^((?![BC]).)*$')