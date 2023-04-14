from src.extract_domain_name.extract_domain_name import (
    extract_domain_name)

def test_returns_a_string():
    result = extract_domain_name("https://github.com")
    assert type(result) == str

def test_returns_the_domain_name_from_a_simple_URL():
    result = extract_domain_name("https://reddit.com")
    assert result == "reddit.com"

def test_returns_the_domain_name_from_a_more_complicated_URL():
    result = extract_domain_name("https://github.com/northcoders/de-py-katas")
    assert result == "github.com"

def test_returns_the_domain_name_from_an_even_more_complicated_URL():
    result = extract_domain_name("https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO9Mrw2_v6AhXtTEEAHWYIBi8Q_AUoAXoECAIQAw&biw=1440&bih=764&dpr=2")
    assert result == "google.com"

def test_returns_the_domain_name_when_the_domain_name_starts_with_w():
    result = extract_domain_name("https://wellthisisamadeupwebsite.com")
    assert result == "wellthisisamadeupwebsite.com"