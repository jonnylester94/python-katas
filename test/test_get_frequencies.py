from src.get_frequencies.get_frequencies import (
    get_frequencies)

def test_returns_an_empty_dictionary_if_passed_an_empty_string():
    expected = {}
    result = get_frequencies('')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_dictionary_with_one_letter_and_value_1_if_passed_a_string_of_one_letter():
    expected = {'a': 1}
    result = get_frequencies('a')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_dictionary_with_key_value_pairs_of_letters_and_frequencies_if_passed_a_string_with_unique_letters():
    expected = {'z': 1, 'e': 1, 'l': 1, 'd':1, 'a' :1}
    result = get_frequencies('zelda')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_dictionary_with_key_value_pairs_of_letters_and_correct_frequencies_if_passed_a_string_with_repeat_letters():
    expected = {'j': 1, 'o': 1, 'n': 2, 'y' :1}
    result = get_frequencies('jonny')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_dictionary_with_key_value_pairs_of_letters_and_correct_frequencies_if_passed_a_multiword_string_with_repeat_letters():
    expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    result = get_frequencies('hello world')
    print(f'Result is: {result}')
    assert result == expected