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

def get_count(s):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - 97] += 1
    return cnt
​
def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    cnt1 = get_count(s1)
    cnt2 = get_count(s2[:len(s1)])
    if cnt1[:] == cnt2[:]:
        return True
    for k in range(len(s1), len(s2)):
        cnt2[ord(s2[k])-97] += 1
        cnt2[ord(s2[k-len(s1)])-97] -= 1
        if cnt1[:] == cnt2[:]:
            return True
    return False

