from src.sum_ascii.sum_ascii import (
    sum_ascii)

def test_returns_a_string():
    result = sum_ascii(['Jonny'])
    assert type(result) == str

def test_returns_the_given_name_if_passed_a_list_of_length_1():
    result = sum_ascii(['Jonny'])
    assert result == 'Jonny'

def test_returns_the_highest_scoring_name_if_passed_a_list_of_length_2():
    result = sum_ascii(['Jonny', 'Mariah'])
    assert result == 'Mariah'

def test_returns_the_highest_scoring_name_if_passed_a_list_of_length_5():
    result = sum_ascii(['Jonny', 'Mariah', 'Grimes', 'Sam', 'Sophia'])
    assert result == 'Grimes'
