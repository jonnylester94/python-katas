from src.alphabet_position.alphabet_position import (alphabet_position)

def test_returns_a_string():
    result = alphabet_position('j')
    assert type(result) == str

def test_returns_correct_string_if_passed_a_single_lower_case_letter():
    result = alphabet_position('a')
    assert result == '1'
    result_two = alphabet_position('e')
    assert result_two == '5'

def test_returns_correct_string_if_passed_multiple_lower_case_letters():
    result = alphabet_position('abc')
    assert result == '1 2 3'
    result_two = alphabet_position('jonny')
    assert result_two == '10 15 14 14 25'

def test_returns_correct_string_if_passed_a_single_upper_case_letter():
    result = alphabet_position('A')
    assert result == '1'
    result_two = alphabet_position('E')
    assert result_two == '5'

def test_returns_correct_string_if_passed_multiple_upper_case_letters():
    result = alphabet_position('ABDF')
    assert result == '1 2 4 6'
    result_two = alphabet_position('AXZ')
    assert result_two == '1 24 26'

def test_returns_correct_string_if_passed_mix_of_upper_and_lower_case_letters():
    result = alphabet_position('AbCGj')
    assert result == '1 2 3 7 10'
    result_two = alphabet_position('aXyZ')
    assert result_two == '1 24 25 26'

def test_returns_correct_string_if_passed_a_sentence_with_white_space_and_full_stop():
    result = alphabet_position('The sunset sets at twelve o\' clock.')
    assert result == '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'