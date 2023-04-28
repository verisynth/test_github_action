import verisynth


def palindrome(original: str) -> bool:
    '''
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    '''
    reversed_string = original[::-1]
    return original == reversed_string


@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """