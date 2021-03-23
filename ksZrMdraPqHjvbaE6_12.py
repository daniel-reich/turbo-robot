"""


Write a function that finds the **largest even number** in a list. Return `-1`
if not found. The use of built-in functions `max()` and `sorted()` are
prohibited.

### Examples

    largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
    
    largest_even([1, 3, 5, 7]) ➞ -1
    
    largest_even([0, 19, 18973623]) ➞ 0

### Notes

Consider using the **modulo operator** `%` or the **bitwise and operator**
`&`.

"""

def largest_even(l):
  def find(l):
    if len(l)==1:return l[0]
    r=find(l[1:]) 
    return r if not r%2 or (r>l[0] and not r%2) else l[0]
  r=find(l)
  return r if not r%2 else -1

