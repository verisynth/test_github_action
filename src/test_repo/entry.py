import verisynth


def palindrome(original: str) -> bool:
    '''
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    '''
    length = len(original)
    for i in range(length // 2):
        if original[i] != original[length - i - 1]:
            return False
    return True



@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """