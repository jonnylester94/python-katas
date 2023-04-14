# working on this one

def caesar(string, number):
    # convert the string to its ascii value
    # add number to the ascii value
    # convert back to character
    # return char

    if number == 0:
        return string

    new_string = ""

    for char in string:
        ascii = ord(char)
        updated_char = chr(ascii + number)
        print(updated_char)
        new_string += updated_char

    print(new_string)
    return new_string
