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

def validate_swaps(values, target):
    '''
    Returns a list of booleans: True if val in values can be formed from target
    by a single swap of 2 character, False otherwise.
    '''
    POSITIONS = {i: target[i] for i in range(len(target))}
    result = []
​
    for val in values:
        if len(val) != len(target) or any(val.count(l) > 1 for l in val):
            swap = False   # must be same length & no duplicates
        else:
            val_idxs = [val.find(char) for _, char in POSITIONS.items()]
            swap = sum(1 for i in range(len(val_idxs)) if val_idxs[i] == sorted(POSITIONS)[i])
            swap = swap == len(target) - 2  # 2 will be different if 1 swap occurred
        result.append(swap)
​
    return result

