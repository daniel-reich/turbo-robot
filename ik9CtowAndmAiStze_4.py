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
​
def frequency_sort(s):
    C = Counter(s)
    A = []
    for c, cnt in C.items():
        A.append([c, ord(c), cnt])
    A.sort(key=lambda x: (-x[2], x[1]))
    ans = ""
    for c, o, cnt in A:
        ans += c * cnt
    return ans

