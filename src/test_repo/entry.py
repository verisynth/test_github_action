import verisynth


def palindrome(original: str) -> bool:
    '''
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    '''
    # Remove any non-alphanumeric characters
    modified = ''.join(filter(str.isalnum, original))
    # Check if modified is the same spelling as reversed string of modified
    return modified == modified[::-1]



@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """