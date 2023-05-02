import pytest
from test_repo.entry import palindrome

def test_palindrome():
    assert palindrome('racecar') == True
    assert palindrome('Hello, world') == False
    assert palindrome('') == True
    assert palindrome('a') == True
    assert palindrome('ab') == False
    assert palindrome('A man a plan a canal Panama') == False
    assert palindrome('Was it a car or a cat I saw?') == False
    assert palindrome('No \'x\' in Nixon') == False
    assert palindrome('Amor, Roma') == False
    assert palindrome('Step on no pets') == False
    assert palindrome('Never odd or even') == False
    assert palindrome('Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.') == False
    assert palindrome('Too hot to hoot.') == False
    assert palindrome('Rise to vote, sir.') == False
    assert palindrome('Do geese see God?') == False
    assert palindrome('Red roses run no risk, on Nurse\'s order.') == False