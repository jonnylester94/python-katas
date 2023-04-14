from src.get_century.get_century import (
    get_century)

def test_returns_the_correct_century_if_passed_a_single_digit():
    expected = '1st'
    result = get_century(1)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_the_correct_century_if_passed_two_digits():
    expected = '1st'
    result = get_century(47)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_the_correct_century_if_passed_three_digits():
    expected = '8th'
    result = get_century(754)
    print(f'Result is: {result}')
    assert result == expected
    
def test_returns_the_correct_century_if_passed_four_digits():
    expected = '19th'
    result = get_century(1877)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_the_correct_century_if_passed_a_different_four_digits():
    expected = '20th'
    result = get_century(1999)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_the_correct_century_if_passed_another_different_four_digits():
    expected = '21st'
    result = get_century(2004)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_the_correct_century_if_passed_the_year_10000():
    expected = '101st'
    result = get_century(10000)
    print(f'Result is: {result}')
    assert result == expected