from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case)

def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    result_two = sentence_to_camel_case('This', True)
    print(f'Result is: {result}')
    assert result == expected
    assert result_two == expected

def test_returns_a_single_word_in_lower_if_false():
    expected = 'this'
    result = sentence_to_camel_case('This', False)
    result_two = sentence_to_camel_case('this', False)
    print(f'Result is: {result}')
    assert result == expected
    assert result_two == expected

def test_returns_a_sentence_in_upper_if_true():
    expected = 'ThisSentence'
    result = sentence_to_camel_case('this sentence', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_sentence_in_lower_if_false():
    expected = 'thisSentence'
    result = sentence_to_camel_case('this sentence', False)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_longer_sentence_in_lower_if_false():
    expected = 'ThisBiggerStrangeSentence'
    result = sentence_to_camel_case('This Bigger strange Sentence', True)
    print(f'Result is: {result}')
    assert result == expected

