"""


Given two non-empty lists, write a function that determines whether the second
list is a subsequence of the first list.

For instance, the numbers `[1, 3, 4]` form a subsequence of the list `[1, 2,
3, 4]`, and so do the numbers `[2, 4]`.

### Examples

    is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) ➞ False
    
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) ➞ True
    
    is_valid_subsequence([1, 2, 3, 4], [2, 4]) ➞ True

### Notes

N/A

"""

def is_valid_subsequence(lst, seq):
​
  #Get rid of obvious failures first:
​
  for l8r in seq:
    if l8r not in lst or lst.count(l8r) < seq.count(l8r):
      return False
  
  #Then find obvious winners:
​
  if seq in lst:
    return True
​
  # To find the rest, get rid of all extraneous numbers in lst!!
​
  nl = [i for i in lst if i in seq]
​
  return seq in nl or seq == nl

