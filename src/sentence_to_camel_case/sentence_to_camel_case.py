def sentence_to_camel_case(arg1, arg2):

    if arg2 == True:
        x = arg1.split()
        comp_capitalized = [word.capitalize() for word in x]
        str1 = ""
        for item in comp_capitalized:
            str1 += item
        return str1
    
    else:
        y = arg1.split()
        comp_capitalized = [word.capitalize() for word in y]
        str2 = ""
        for item in comp_capitalized:
            str2 += item
        return str2[0].lower() + str2[1:]


    
  