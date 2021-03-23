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
  a, b='', ''
  for x in s:
    if x in t:
      a+=x
    else:
      b+=x
  return ''.join(sorted(a, key=lambda x: t.index(x))+sorted(b))

