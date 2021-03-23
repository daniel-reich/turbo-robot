"""


Given a string `text`. Write a function that returns the character with the
highest frequency. If more than 1 character has the same highest frequency,
return all those characters as an array sorted in ascending order. If there is
no repetition in characters, return `"No Repetition"`.

### Examples

    max_occur("Computer Science") ➞ ['e']
    
    max_occur("Edabit") ➞ "No Repetition"
    
    max_occur("system admin") ➞ ['m', 's']
    
    max_occur("the quick brown fox jumps over the lazy dog") ➞ [' ']

### Notes

Try to make use of the concept used in counting sort.

"""

from collections import*
def max_occur(t):
  d=Counter(t).most_common()
  m=d[0][1]
  if m==1:return'No Repetition'
  l=[d[0][0]]
  for x in d[1:]:
    if x[1]!=m:break
    l.append(x[0])
  return sorted(l)

