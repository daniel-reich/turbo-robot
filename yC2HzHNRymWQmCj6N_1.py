"""


 **Mubashir** needs your help in a simple task.

Given a list of integers `lst` and an integer `k`, find the lowest positive
integer **x** so that exactly **k elements of the given list are _less than or
equal_ to x.** Return `None` if the condition does not match.

See below examples for a better understanding:

### Examples

    less_or_equal([3, 7, 6, 1, 10, 3, 20], 4) ➞ 6
    # 1, 3, 3, 6 = 4 elements
    # All elements are less than or equal to 6
    
    less_or_equal([3, 7, 6, 1, 10, 3, 20], 2) ➞ None
    # 1, 3 = 2 elements
    # Not possible to return 3 because we have another 3 in the list
    
    less_or_equal([3, 7, 5, 1, 10, 3, 20], 4) ➞ 5
    # 1, 3, 3, 5 = 4 elements
    # All elements are less than or equal to 5
    
    less_or_equal([10, 15, 20, 25], 0) ➞ 1
    # k = 0

### Notes

  * All numbers of the given list and k will be ≥ 0.
  * Understanding the description of this challenge is the hardest part.

"""

def less_or_equal(lst, k):
  if len(lst) == k:
    return lst[-1]
​
  for x in range(1,9):
    if sum(1 for n in lst if x >= n) == k:
      return x

