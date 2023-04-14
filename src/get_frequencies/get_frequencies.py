def get_frequencies(string):

	updated_string = string.replace(' ', '')
	
	new_dictionary = {}

	for letter in updated_string:
		if letter not in new_dictionary:
			new_dictionary[letter] = 1
		else: 
			new_dictionary[letter] += 1

	return new_dictionary

