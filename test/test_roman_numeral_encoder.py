from src.roman_numeral_encoder.roman_numeral_encoder import (
    roman_numeral_encoder)

def test_returns_a_string():
    result = roman_numeral_encoder(3)
    assert type(result) == str

def test_returns_correct_string_when_passed_a_number_less_than_4():
    result_one = roman_numeral_encoder(1)
    result_two = roman_numeral_encoder(3) 
    assert result_one == 'I'
    assert result_two == 'III'

def test_returns_correct_string_when_passed_a_number_less_than_10_but_greater_than_3():
    result_one = roman_numeral_encoder(6)
    result_two = roman_numeral_encoder(7) 
    assert result_one == 'VI'
    assert result_two == 'VII'

def test_returns_correct_string_when_passed_a_number_between_10_and_50():
    result_one = roman_numeral_encoder(13)
    result_two = roman_numeral_encoder(27) 
    result_three = roman_numeral_encoder(42)
    result_four = roman_numeral_encoder(45)  
    assert result_one == 'XIII'
    assert result_two == 'XXVII'
    assert result_three == 'XLII'
    assert result_four == 'XLV'


def test_returns_correct_string_when_passed_a_bigger_number():
    result_one = roman_numeral_encoder(156)
    result_two = roman_numeral_encoder(444) 
    result_three = roman_numeral_encoder(712)
    result_four = roman_numeral_encoder(999)  
    assert result_one == 'CLVI'
    assert result_two == 'CDXLIV'
    assert result_three == 'DCCXII'
    assert result_four == 'CMXCIX'