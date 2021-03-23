"""


Given an array of strings and an original string, write a function to output
an array of boolean values - `True` if the word can be formed from the
original word by swapping two letters **only once** and `False` otherwise.

### Examples

    validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE")
    ➞ [True, True, False, False]
    
    # Swap "A" and "B" from "ABCDE" to get "BACDE".
    # Swap "A" and "E" from "ABCDE" to get "EBCDA".
    # Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap.
    
    validate_swaps(["32145", "12354", "15342", "12543"], "12345")
    ➞ [True, True, True, True]
    
    validate_swaps(["9786", "9788", "97865", "7689"], "9768")
    ➞ [True, False, False, False]

### Notes

Original string will consist of unique characters.

"""

from collections import Counter
​
def check(word1, word2):
    if len(word1) != len(word2):
        return False
    diffs = [i for i in range(len(word1)) if word1[i] != word2[i]]
    if len(diffs) == 0:
        return True
    if len(diffs) != 2:
        return False
    return Counter(word1) == Counter(word2)
​
def validate_swaps(lst, txt):
    return [check(elem, txt) for elem in lst]

