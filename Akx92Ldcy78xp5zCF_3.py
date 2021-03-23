"""


The function is given two strings `t` \- template, `s` \- to be sorted. Sort
the characters in `s` such that if the character is present in `t` then it is
sorted according to the order in `t` and other characters are sorted
alphabetically after the ones found in `t`.

### Examples

    custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"
    
    custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"
    
    custom_sort("", "abcdefzyx") ➞ "abcdefxyz"
    
    custom_sort("", "") ➞ ""

### Notes

The characters in `t` and `s` are all lower-case.

"""

def custom_sort(t, s):
    seq = {}
    k = 0
    for c in t:
        seq[k] = c
        k += 1
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in t:
            seq[k] = c
            k += 1
    ans = ""
    for i in range(26):
        ans += seq[i] * s.count(seq[i])
    return ans

