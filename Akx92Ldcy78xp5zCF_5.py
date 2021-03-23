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
  nt =  [l8r for l8r in t if l8r in s]
  ns = []
  
  for l8r in set(s):
    if l8r in nt:
      tcount = t.count(l8r)
      scount = s.count(l8r)
      for n in range(scount - tcount):
        nt = nt[:nt.index(l8r)] + [l8r] + nt[nt.index(l8r):]
    else:
      for n in range(s.count(l8r)):
        ns.append(l8r)
  
  return ''.join(nt) + ''.join(sorted(ns))

