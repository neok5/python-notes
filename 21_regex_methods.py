#
# REGULAR EXPRESSIONS METHODS
#
#	- They are character sequences that conforms a search pattern, useful in
#	 text processing tasks, a very common matter in any application.
#
#	- To use regex in Python we have to use the built-in module 're'. Utilities:
#
#		· search(seeked_str, str[, flags]):
#			+ seeked_str: string searched in {str}
#			+ str: string where the {seeked_str} is searched
#			+ flags: optional commands that can modify the meaning of the regex
#				(to use several of them we must build the argument separating them with '|')
#				re.MULTILINE - re.M - apply '^' and '$' to each line in the string
#				re.IGNORECASE - re.I - check regardless upper or lower case
#				re.DOTALL - re.S - '.' matches anything INCLUDING newline characters
#
#			+ Returns None if the 'seeked_str' doesn't exist in the string,
#			 or a 're.Match' object if it finds it.
#
#		· findall(seeked_str, str):
#			+ Returns a list with all the matches between 'seeked_str' and 'str',
#			 so we can measure list size to count how many times 'str' was found
#
#		· match(seeked_str, str[, flags]):
#			+ While search() searches the entire string, match() is anchored
#			 at the beginning of the string, so it only will success if the
#			 match occurs at the very start of the string we're searching in
#
#			+ Returns None if the 'seeked_str' doesn't exist in the string start,
#			 or a 're.Match' object if it finds it at the beginning of the string.
#
#		· 're.Match' object contains, among others:
#			+ a 'match' field: a 'str' with the found text.
#			+ a 'span' field: a tuple with starting and ending index of str found.
#			+ we can access its values through several functions over the
#			 object like 'start' (of the span), 'end' (of the span) or 'span' (both);
#			  we can also use 're' or 'string' to access those fields respectively;
#			 and finally we can use group([group_index,]) (defaults to 0), to get the
#			  specified captured group, or groups() to get them all (if more than one)
#
#	- We can use anchors (^ - line_start, and $ - line_end) to make more accurate searches.
#
#	- There are also 'character classes' or 'character sets' which serve to tell the regex
#	 engine to match only one of several characters. The characters to match must be put
#	 into square brackets. Example: 'gr[ae]y' match either 'gray' or 'grey', but not 'graey'.
#
import re

print("----------------------- Searching words ------------------------\n")

text = 'Lore ipsum dolor sit amet'
word = 'ipsum do'
other_word = 'egfkjsbds'
part = 'or'

def exists_word(_word, _text):
	return 'does' if re.search(_word, _text) is not None else 'doesn\'t'

print(f'''\tText: \'{text}\'
	Word: \'{word}\'
	Other word: \'{other_word}\'
	Part: \'{part}\'\n''')

search_result = exists_word(word, text)
start = re.search(word, text).start()
end = re.search(word, text).end()
print(f'\t· The word {search_result} exist in the text and goes from {start} to {end}')
print(f'\t· The other word {exists_word(other_word, text)} exist in the text')

find_result = re.findall(part, text)
print(f'\t· The part appears {len(find_result)} times in the text: {find_result}')
print()

print("----------------------- Filtering urls ------------------------\n")

urls = ['https://www.google.es', 'http://as.com', 'https://www.xataka.com']

def show_filtered_urls(_list, pattern):
	for _elem in _list:
		if re.findall(pattern, _elem):
			print(f' [{_elem}]', end='')
	print()

print(f'\t->\tURLs list:', end='')
show_filtered_urls(urls, '')  # with an empty pattern, it return the whole list

print(f'\n\t->\tHTTP secure domains:', end='')
show_filtered_urls(urls, '^https://')

print(f'\n\t->\t\'.es\' domains:', end='')
show_filtered_urls(urls, '.es$')

print(f"\n\t->\tUrls containing 'x' letter:", end='')
show_filtered_urls(urls, '[x]')

print(f"\n\t->\t'g' or 'o' letter appearances in first url:", end='')
show_filtered_urls(urls[0], '[go]')
print()
