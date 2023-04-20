import re

def extract_domain_name(URL):

	x = re.findall("h.+.com", URL)
	URL_two = x[0]

	sliced = URL_two[8:]

	if sliced[0] and sliced[1] and sliced[2] == 'w':
		return sliced[4:]
	else:
		return sliced

	