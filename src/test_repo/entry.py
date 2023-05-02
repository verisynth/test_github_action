import verisynth


def palindrome(original: str) -> bool:
    """
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    """
    return original == original[::-1]


def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """
    if n < 0:
        n = abs(n)
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)
    return sum_digits