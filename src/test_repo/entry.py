import verisynth


def palindrome(original: str) -> bool:
    """
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    """
    # Method 1 - By comparing original with reverse of original string
    # If both are same, original is a Palindrome.
    if original == original[::-1]:
        return True
    else:
        return False

    # Method 2 - By comparing original for the first half of characters with the last half of characters
    # One additional check is required for strings with odd length
    # If both are same, original is a Palindrome.
    # last_half is made by starting from the middle and going till the end of the original string and reversing it
    last_half = original[(len(original)+1)//2:][::-1]
    if original[:len(original)//2] == last_half:
        return True
    else:
        return False


@verisynth.completion()
def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """