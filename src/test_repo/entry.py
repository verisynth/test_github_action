import verisynth


def palindrome(original: str) -> bool:
    return original == original[::-1]


@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """