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

from collections import Counter
def frequency_sort(s):
    cnt = [(k, v) for k, v in Counter(s).items()]
    cnt.sort(key=lambda t: (-t[1], t[0]))
    return "".join(t[0] * t[1] for t in cnt)

