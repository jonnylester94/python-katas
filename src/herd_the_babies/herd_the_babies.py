def herd_the_babies(string):

    babies_list = []
    parents_list = []

    for letter in string:
        if letter.islower():
            babies_list.append(letter)
        else:
            parents_list.append(letter)

    sorted_babies = sorted(babies_list)
    sorted_parents = sorted(parents_list)

    for letter in sorted_babies:
        if letter.upper() not in sorted_parents:
            sorted_parents.append(letter)
        else:
            letter_index = sorted_parents.index(letter.upper()) + 1
            sorted_parents.insert(letter_index, letter)
    
    print(sorted_parents)

    final_string = ""
    for char in sorted_parents:
        final_string += char
    
    return final_string


            

