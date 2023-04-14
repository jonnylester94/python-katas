def sum_ascii(list):

# 1. convert each name in the list into lowercase
# 2. find ascii value of each char in name
# 3. sum these values to create total for each name 
# 4. find index of highest number
# 5. use that index to return correct name from original list

    numbers_list = []

    for name in list:
        lowercase_name = name.lower()
        ascii_values = [ord(char) for char in lowercase_name]
        print(ascii_values)
        total = sum(ascii_values)
        print(total)
        numbers_list.append(total)

    print(numbers_list)
    index = numbers_list.index(max(numbers_list))
    return list[index]
