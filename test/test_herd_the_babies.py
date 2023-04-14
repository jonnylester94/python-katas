from src.herd_the_babies.herd_the_babies import (
    herd_the_babies)

def test_returns_a_string():
    result = herd_the_babies('a')
    assert type(result) == str
    result_two = herd_the_babies('iiiI')
    assert type(result_two) == str

def test_returns_string_of_parent_letter_then_baby_letter_if_passed_a_string_of_the_same_letter():
    result = herd_the_babies('aA')
    assert result == 'Aa'

def test_returns_string_in_alphabetical_order_with_parent_letter_before_baby_letter_if_passed_a_string_of_two_different_letter():
    result = herd_the_babies('aBA')
    assert result == 'AaB'

def test_returns_string_in_the_right_format_if_passed_a_more_complicated_string():
    result = herd_the_babies('bbaBccAC')
    assert result == 'AaBbbCcc'

def test_returns_string_in_the_right_format_if_passed_a_different_more_complicated_string():
    result = herd_the_babies('jakpbpJaBAKP')
    assert result == 'AaaBbJjKkPpp'