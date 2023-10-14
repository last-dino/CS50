from twttr import shorten

def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_mixed():
    assert shorten("The year is 2023.") == "Th yr s 2023."
