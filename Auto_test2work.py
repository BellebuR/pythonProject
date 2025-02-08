import pytest
from Auto_test2 import count_vowels

def test_all_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0

def test_mixed_strings():
    assert count_vowels("Hello World") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 4
    assert count_vowels("123 abc!") == 1

if __name__ == "__main__":
    pytest.main()