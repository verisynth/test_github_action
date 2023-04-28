import pytest
from test_repo.entry import palindrome

def test_palindrome():
    assert palindrome("racecar")
    assert not palindrome("hello")