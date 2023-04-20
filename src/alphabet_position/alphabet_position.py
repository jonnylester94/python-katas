def alphabet_position(string):

    new_list = list(string)

    new_string = ""
    for char in new_list:
            num = ord(char.lower()) - 96
            if num < 27 and num > 0:
                new_string += f"{str(num)}," 


    final_str = new_string.replace(",", " ")
    return final_str.strip()



