"""


The function is given two strings `s1` and `s2`. Determine if one of the
permutations of characters of `s1` is a substring of `s2`, return `True /
False`.

### Examples

    check_inclusion("ab", "edabitbooo") ➞ True
    # "ab" is in s2.
    
    check_inclusion("ab", "edaoboat") ➞ False
    # neither "ab" or "ba" is in s2.
    
    check_inclusion("adc", "dcda") ➞ True
    # "cda" is a permutation of "adc" and it is in s2.
    
    check_inclusion("sgyuws", "oldqwqdmlvsguswyfbj") ➞ True
    # "sguswy" is a permutation of s1 and it is in s2.

### Notes

All characters in both strings are lowercase letters.

"""

def check_inclusion(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    arr1 = [0] * 26
    for c in s1:
        idx = ord(c) - 97
        arr1[idx] += 1
    arr2 = [0] * 26
    for c in s2[:len_s1]:
        idx = ord(c) - 97
        arr2[idx] += 1
    if arr1 == arr2:
        return True
    for i in range(len_s2 - len_s1):
        left = ord(s2[i]) - 97
        arr2[left] -= 1
        right = ord(s2[i + len_s1]) - 97
        arr2[right] += 1
        if arr1 == arr2:
            return True
    return False

