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



