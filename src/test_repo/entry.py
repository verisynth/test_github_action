import verisynth


def palindrome(original: str) -> bool:
    '''
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    '''
    # Use slicing to reverse the string and compare to original.
    return original == original[::-1]


@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """