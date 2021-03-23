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

def validate_swaps(lst, txt):
    res = []
    for word in lst:
        if len(word) > len(txt) or sorted(word) != sorted(txt):
            res.append(False)
            continue
        letters, s = list(word), list(txt)
        indexes = [word.index(c) for c in txt if txt.index(c) != word.index(c)]
        if len(indexes) > 2 or len(indexes) < 2:
            res.append(False)
            continue
        letters[indexes[0]], letters[indexes[1]] = letters[indexes[1]],letters[indexes[0]]
        if letters == s:
            res.append(True)
        else:
            res.append(False)
    return res

