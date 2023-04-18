def caesar(string, number):
    
    if number == 0:
        return string

    new_string = ""

    for char in string:
        if char.islower():
            ascii = ord(char)
            new_ascii_num = ascii + number
            if new_ascii_num > 122:
                new_ascii_num -= 26
            elif new_ascii_num < 97:
                new_ascii_num += 26
            updated_char = chr(new_ascii_num)
            new_string += updated_char
        else:
            ascii = ord(char)
            new_ascii_num = ascii + number
            if new_ascii_num > 90:
                new_ascii_num -= 26
            elif new_ascii_num < 65:
                new_ascii_num += 26
            updated_char = chr(new_ascii_num)
            new_string += updated_char

    return new_string
