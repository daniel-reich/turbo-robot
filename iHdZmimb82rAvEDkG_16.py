"""


Write a function that returns the largest even integer in a list with its
corresponding index and the parity of that index, but determining the parity
of that index is **limited to not using** the **modulo operator** `%`.

### Output Structure:

    {"@odd|even index " + index_of_largest: largest_integer}

### Examples

    bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}
    
    bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}
    
    bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}
    
    bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"

### Notes

  * The use of `index()` and `max()` are restricted.
  * If there are no even integers, return `"No even integer found!"`.
  * The set of limitations imposed on this challenge dictates the level of difficulty.
  * Another version of this challenge that deals with recursion can be [found here](https://edabit.com/challenge/pMbki4f2BA8R5vbXs).

"""

def even(a):
    return (a & 1)
def bitwise_index(lst):
  p={}
  for i in range(len(lst)):
    if even(lst[i])==0 and lst[i]>=0 and lst[i] not in p: p[lst[i]]=i
    else: pass
  if len(p)==0:
    d1="No even integer found!"
  elif even(p[max(p)])==0:
    x1='@even index '+str(p[max(p)])
    d1={x1:max(p)}
  else:
    x2='@odd index '+str(p[max(p)])
    d1={x2:max(p)}
  return d1

