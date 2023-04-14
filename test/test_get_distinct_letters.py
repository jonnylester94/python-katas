from src.get_distinct_letters.get_distinct_letters import (
    get_distinct_letters)


def test_returns_one_letter_if_passed_the_same_letter_for_each_string():
    expected = 'j'
    result = get_distinct_letters('j', 'j')
    print(f'Result is: {result}')
    assert result == expected
    
def test_returns_two_letters_in_alphabetical_order_if_passed_a_different_letter_for_each_string():
    expected = 'ac'
    result = get_distinct_letters('a', 'c')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_string_in_alphabetical_order_if_all_the_letters_in_both_strings_are_unique():
    expected = 'adehlnoptyz'
    result = get_distinct_letters('python', 'zelda')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_string_in_alphabetical_order_of_only_the_unique_letters():
    expected = 'ehjy'
    result = get_distinct_letters('hello', 'jonny')
    print(f'Result is: {result}')
    assert result == expected
