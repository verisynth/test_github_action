import pytest
from test_repo.entry import palindrome

def test_palindrome():
    assert palindrome('racecar') == True
    assert palindrome('hello') == False
    assert palindrome('a') == True
    assert palindrome('') == True
    assert palindrome('Able ,wAs I eRE I saw Elba') == False

if __name__ == '__main__':
    pytest.main(['-v'])