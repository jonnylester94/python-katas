from src.lengthen_date.lengthen_date import (
    lengthen_date)

def test_returns_date_in_correct_format_for_current_date():
    expected = 'Wednesday 22nd February 2023'
    result = lengthen_date('22.02.2023')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_date_in_correct_format_for_first_day_of_year():
    expected = 'Wednesday 01st January 2020'
    result = lengthen_date('01.01.2020')
    print(f'Result is: {result}')
    assert result == expected
    
def test_returns_date_in_correct_format_for_my_birthday():
    expected = 'Thursday 29th September 1994'
    result = lengthen_date('29.09.1994')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_date_in_correct_format_for_mariah_careys_birthday():
    expected = 'Thursday 27th March 1969'
    result = lengthen_date('27.03.1969')
    print(f'Result is: {result}')
    assert result == expected