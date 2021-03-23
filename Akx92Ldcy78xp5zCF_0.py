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
    set_t = set(ord(c) for c in t)
    d = {c: i for i, c in
         enumerate(list(t) + [chr(i) for i in range(97, 123)
                              if i not in set_t])}
    return "".join(sorted(list(s), key=lambda c: d[c]))

