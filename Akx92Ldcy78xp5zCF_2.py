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
    aux = ''
    for c1 in s:
        if c1 in t:
            aux += c1
            s = s.replace(c1, '')
    aux2 = ''
    for c2 in t:
        for c3 in aux:
            if c2 == c3:
                aux2 += c3
    return aux2 + ''.join(sorted(s))

