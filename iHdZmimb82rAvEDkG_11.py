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

def first_even(lst):
  for i in range(len(lst)):
    if parity(lst[i]) == 0:
      return [lst[i], i]
  return False
​
def parity(n):
  return n - ((n >> 1) << 1)
​
def bitwise_index(lst):
  has_even = first_even(lst)
  if has_even == False:
    return 'No even integer found!'
  else:
    cur_largest = has_even[0]
    large_ind = has_even[1]
  for i in range(len(lst)):
    if lst[i] > cur_largest and parity(lst[i]) == 0:
      cur_largest = lst[i]
      large_ind = i
  if parity(large_ind) == 0:
    s = '@even'
  else:
    s = '@odd'
  s = s + ' index ' + str(large_ind)
  return {s:cur_largest}

