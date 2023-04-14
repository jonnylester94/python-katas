from src.create_counter.create_counter import (
    create_counter)

def test__returns_dictionary_with_correct_keys():
    result = create_counter(0)
    assert 'up' in result
    assert 'down' in result

def test_up_function_returns_given_number_incremented():
    result = create_counter(5)
    assert result['up']() == 6

def test_down_function_returns_given_number_incremented():
    result = create_counter(5)
    assert result['down']() == 4

def test_number_is_not_reset_for_each_invocation_of_up_function():
    result = create_counter(3)
    result['up']()
    assert result['up']() == 5

def test_number_is_not_reset_for_each_invocation_of_down_function():
    result = create_counter(12)
    result['down']()
    assert result['down']() == 10


# SEMINAR:
# between invocations of up and down the count is saved (ie its not being reset)
# test1: need to test that the correct keys (up) are being returned in the dictionary - so need a method that is about checking if key exists... assert 'up' in test_counter
# test2: test 'up' returns incremented number
# test3: if you invoke twice, it should go up twice - so will need to invoke twice in tests
