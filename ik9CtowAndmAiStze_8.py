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
  is_upper = [True,False]
  chars = [char for char in s]
  chars.sort()
  chars.sort(key = lambda x: is_upper.index(x.isupper()))
  chars.sort(key = lambda x: s.count(x),reverse = True)
  return ''.join(chars)

