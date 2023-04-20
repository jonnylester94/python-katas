def get_distinct_letters(str1, str2):

	if str1 == str2:
		return str1
	else:
		combined_string = str1 + str2
		new_string = ""
		for letter in combined_string:
			if combined_string.count(letter) == 1:
				new_string += letter	
		a = sorted(new_string)
		return ''.join(a)


