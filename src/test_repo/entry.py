import verisynth


def palindrome(original: str) -> bool:
    '''
    Return True if `original` is a palindrome (case sensitive), False otherwise.

    Parameters:
    original (str): a string to check if it's a palindrome.

    Returns:
    bool: True if `original` is a palindrome, False otherwise.
    '''
    # Remove whitespaces
    original = original.replace(' ', '')
    # Compare original with its reverse
    return original == original[::-1]



@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """