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

from collections import Counter as C
def frequency_sort(s):
  A=[x*C(s)[x] for x in C(s)]
  A=sorted(A, key=lambda x: (-len(x), x[0]))
  return ''.join(A)

