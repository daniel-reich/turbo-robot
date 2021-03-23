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
  f={x:s.count(x)for x in sorted(s)}
  return''.join(sorted(s,key=lambda x:(-f.get(x),x)))

