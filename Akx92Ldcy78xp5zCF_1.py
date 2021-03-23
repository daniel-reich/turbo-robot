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
  if t == '': return ''.join(sorted(s))
  res1 = ''.join(sorted([i for i in s if i in t], key=lambda x: t.index(x)))
  res2 = ''.join(sorted([i for i in s if i not in t]))
  result = res1 + res2
  return result

