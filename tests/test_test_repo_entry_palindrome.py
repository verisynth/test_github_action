import pytest
from test_repo.entry import palindrome

def test_empty_string():
    assert palindrome('')

def test_palindrome():
    assert palindrome('racecar')

def test_non_palindrome():
    assert not palindrome('hello')
    assert not palindrome('world')
    assert not palindrome('1234')
    assert not palindrome('1221 ') 
