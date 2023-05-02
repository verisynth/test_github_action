import pytest
from test_repo.entry import palindrome
def test_palindrome():
    assert palindrome('racecar') == True
    assert palindrome('hello') == False
    assert palindrome('A man a plan a canal Panama') == False
    assert palindrome('Was it a car or a cat I saw') == False