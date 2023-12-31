from working import convert
import unittest

def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
        convert("9 AM - 5 PM")
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
        convert("09:00 AM - 17:00 PM")

def test_value():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
        convert("9:60 AM to 5:60 PM")