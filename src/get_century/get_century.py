import math
def get_century(year):

    if year < 100:
        return '1st'
    
    elif year == 10000:
        return '101st'

    else:
       century = math.ceil(year / 100)

    string_century = str(century)

    if string_century.endswith('1'):
        return f'{string_century}st'

    elif string_century.endswith('2'):
        return f'{string_century}nd'
        
    elif string_century.endswith('3'):
        return f'{string_century}rd'

    else:
        return f'{string_century}th'



    # 0 - 99 --> 1st
    # 100 - 199 --> 2nd
    # 200 - 299 --> 3rd
    # 1000 - 1099 --> 11th
    # 1100 - 1199 --> 12th
    # 1200 - 1299 --> 13th
    # 1900 - 1999 --> 20th
    # 2000 - 2099 --> 21st

