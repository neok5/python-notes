my_dict = { "Germany" : "Berlin", # declaration and definition; JSON / JS objects
	"France" : "Paris", "United Kingdom" : "London"}
print(my_dict) # access all elements
print(my_dict["France"]) # access one element using it key
print()
print('-----------------------------------------------------------------')

# special way to acces a dictionary
# using get(dict_key[, default_value = None])
print(my_dict.get("Germany"))
print(my_dict.get("German"))
print(my_dict.get("German", None))
print(my_dict.get("German", "Incorrect key!"))
print()
print('-----------------------------------------------------------------')

my_dict["Italy"] = "wegrgsds" # add a new element
print(my_dict)
my_dict["Italy"] = "Rome" # edit an existing element
print(my_dict)
del my_dict["United Kingdom"] # remove an element, not return anything
print(my_dict)
country_capital = my_dict.pop('Italy') # remove and return an element
print(f'Italy out! {country_capital}') # return only the value of deleted key
print(my_dict)
print()

mutivalued_type_dict = { "first" : 1, 2.5555 : "second"}
print(mutivalued_type_dict) # a dict can have several values as key or value
print()
print('-----------------------------------------------------------------')

my_tuple = ["Russia", "China", "Japan"]
reducted_dict = {
	my_tuple[0] : "Moscow", my_tuple[1] : "Beijing", my_tuple[2] : "Kyoto" }
print(reducted_dict) # a tuple can be used as collection of keys for a dictionary
print(reducted_dict["Russia"]) # you can also use a tuple to access dict elements
print(reducted_dict[my_tuple[0]])
print()
print('-----------------------------------------------------------------')

dict_with_complex_types = { # a dict can contain lists, tuples or another dicts
	23 : "Jordan",
	"name" : "Michael",
	"prizes" : [ 1991, 1992, 1993, 1996, 1997, 1998],
	"fortune" : {
		"cash" : 50000,
		"properties" : 2000000
	}
}
print("Complete\n", dict_with_complex_types)
print("Prizes\n", dict_with_complex_types["prizes"])
print("Fortune\n", dict_with_complex_types["fortune"])
print()
print('-----------------------------------------------------------------')

print(dict_with_complex_types.keys()) # show dictionary keys
print(dict_with_complex_types.values()) # show dictionary values
print(dict_with_complex_types.items()) # show dictionary entries
print(len(dict_with_complex_types)) # show dictionary size
print()

for key, value in dict_with_complex_types.items():
	print(f'{key} -> {value}')