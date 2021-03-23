"""


The function is given a string. Sort the characters and return a new string.
Sorting conditions:

  * Most frequent move in front.
  * For the same frequency upper case characters move in front.
  * For the same frequency and case sort them alphabetically.

### Examples

    frequency_sort("tree") ➞ "eert"
    
    frequency_sort("cccaaa") ➞ "aaaccc"
    
    frequency_sort("Aabb") ➞ "bbAa"

### Notes

N/A

"""

def frequency_sort(s):
  d = {}
  for c in s:
    d[c] = d.get(c, 0) + 1
  return ''.join([k * v for k, v in sorted(d.items(), key=lambda e: (-e[1], e[0]))])

