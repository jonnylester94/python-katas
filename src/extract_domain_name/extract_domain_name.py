import re

def extract_domain_name(URL):

	x = re.findall("h.+.com", URL)
	print(x)
	URL_two = x[0]

	sliced = URL_two[8:]
	print(sliced)

	if sliced[0] and sliced[1] and sliced[2] == 'w':
		print(sliced[4:])
		return sliced[4:]
	else:
		return sliced

	