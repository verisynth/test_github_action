import pytest
from test_repo.entry import palindrome

def test_palindrome():
    assert palindrome('racecar') == True
    assert palindrome('level') == True
    assert palindrome('hello') == False
    assert palindrome('Was it a car or a cat I saw?') == False
    assert palindrome('No \'x\' in Nixon') == False