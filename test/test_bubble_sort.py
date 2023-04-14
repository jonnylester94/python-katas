from src.bubble_sort.bubble_sort import (
    bubble_sort)

def test_returns_a_list():
    result = bubble_sort([1, 2])
    assert type(result) == list

def test_correctly_sorts_a_list_of_length_2():
    result_one = bubble_sort([2, 1])
    result_two = bubble_sort([3, 1])
    result_three = bubble_sort([1, 2])
    result_four = bubble_sort([1, 3])
    assert result_one == [1, 2]
    assert result_two == [1, 3]
    assert result_three == [1, 2]
    assert result_four == [1, 3]

def test_correctly_sorts_a_list_of_length_3():
    result_one = bubble_sort([2, 1, 4])
    result_two = bubble_sort([5, 8, 2])
    assert result_one == [1, 2, 4]
    assert result_two == [2, 5, 8]

def test_correctly_sorts_a_list_of_length_5():
    result = bubble_sort([2, 1, 4, 9, 3])
    assert result == [1, 2, 3, 4, 9]
