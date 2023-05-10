from test_repo.entry import sum_of_digits
def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(456) == 15
    assert sum_of_digits(789) == 24
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-123) == 6
    assert sum_of_digits(-456) == 15
    assert sum_of_digits(-789) == 24