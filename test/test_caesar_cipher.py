# working on this one

from src.caesar_cipher.caesar_cipher import (
    caesar)

def test_returns_a_string():
    result = caesar('a', 0)
    assert type(result) == str

def test_returns_the_given_string_when_N_equals_zero():
    result_one = caesar('a', 0)
    result_two = caesar('Jonny', 0)
    result_three = caesar('Mariah_Carey', 0)
    assert result_one == 'a'
    assert result_two == 'Jonny'
    assert result_three == 'Mariah_Carey'

def test_returns_the_correct_string_when_passed_a_string_of_length_1_and_N_is_positive():
    result_one = caesar('a', 1)
    result_two = caesar('j', 5)
    result_three = caesar('m', 11)
    assert result_one == 'b'
    assert result_two == 'o'
    assert result_three == 'x'

def test_returns_the_correct_string_when_passed_a_longer_string_and_N_is_positive():
    result_one = caesar('hello', 3)
    # result_two = caesar('jonny', 5)
    # result_three = caesar('mariah', 11)
    assert result_one == 'khoor'
    # assert result_two == ''
    # assert result_three == ''

