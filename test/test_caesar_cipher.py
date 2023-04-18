from src.caesar_cipher.caesar_cipher import (
    caesar)

def test_returns_a_string():
    result = caesar('a', 0)
    assert type(result) == str

def test_returns_the_given_string_when_N_equals_zero():
    result_one = caesar('a', 0)
    result_two = caesar('jonny', 0)
    result_three = caesar('mariah_carey', 0)
    assert result_one == 'a'
    assert result_two == 'jonny'
    assert result_three == 'mariah_carey'

def test_returns_the_correct_string_when_passed_a_string_of_length_1_and_N_is_positive():
    result_one = caesar('a', 1)
    result_two = caesar('j', 5)
    result_three = caesar('m', 11)
    assert result_one == 'b'
    assert result_two == 'o'
    assert result_three == 'x'

def test_returns_the_correct_string_when_passed_a_longer_string_and_N_is_positive():
    result_one = caesar('hello', 3)
    result_two = caesar('mariah', 6)
    result_three = caesar('utah', 8)
    assert result_one == 'khoor'
    assert result_two == 'sgxogn'
    assert result_three == 'cbip'

def test_returns_the_correct_string_when_passed_a_string_of_length_1_and_N_is_negative():
    result_one = caesar('b', -1)
    result_two = caesar('o', -5)
    result_three = caesar('x', -11)
    assert result_one == 'a'
    assert result_two == 'j'
    assert result_three == 'm'

def test_returns_the_correct_string_when_passed_a_longer_string_and_N_is_negative():
    result_one = caesar('hello', -3)
    result_two = caesar('jonny', -5)
    result_three = caesar('bat', -7)
    assert result_one == 'ebiil'
    assert result_two == 'ejiit'
    assert result_three == 'utm'

def test_returns_the_correct_string_when_passed_a_mix_of_capitals_and_non_capitals():
    result_one = caesar('hEllo', 3)
    result_two = caesar('JONNY', -5)
    result_three = caesar('bAt', -8)
    assert result_one == 'kHoor'
    assert result_two == 'EJIIT'
    assert result_three == 'tSl'