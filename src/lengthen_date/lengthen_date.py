from datetime import datetime

def lengthen_date(date):

    new_date = date.replace('.', '/')

    object_date = datetime.strptime(new_date, '%d/%m/%Y')

    weekday = object_date.strftime('%A')
    day = object_date.strftime('%d')
    month = object_date.strftime('%B')
    year = object_date.strftime('%Y')

    # ordinal thing
    if day.endswith('1'):
        updated_day = f'{day}st'

    elif day.endswith('2'):
        updated_day = f'{day}nd'

    elif day.endswith('3'):
        updated_day = f'{day}rd'

    else:
        updated_day = f'{day}th'

    joined_string = f'{weekday} {updated_day} {month} {year}'
    return joined_string



