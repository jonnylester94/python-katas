from src.years_of_growth.years_of_growth import (
    years_of_growth)

def test__returns_an_integer():
    result = years_of_growth(100, 200, 1, 2)
    assert type(result) == int
    result_two = years_of_growth(5, 5000, 30, 4)
    assert type(result_two) == int

def test__returns_0_when_end_population_is_no_bigger_than_starting_population():
    result = years_of_growth(2000, 2000, 10, 35)
    assert result == 0
    result_two = years_of_growth(1000, 970, 3, 200)
    assert result_two == 0

def test__returns_correct_number_of_years_for_given_input():
    result = years_of_growth(1000, 2000, 2, 12)
    assert result == 25

def test__returns_correct_number_of_years_for_a_different_input():
    result = years_of_growth(2000, 2010, 10, 35)
    assert result == 1

def test__returns_correct_number_of_years_for_another_different_input():
    result = years_of_growth(2000, 4000, 1, 20)
    assert result == 41



