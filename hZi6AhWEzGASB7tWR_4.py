"""


Write a function that takes a list and determines whether it's strictly
increasing, strictly decreasing, or neither.

### Examples

    check([1, 2, 3]) ➞ "increasing"
    
    check([3, 2, 1]) ➞ "decreasing"
    
    check([1, 2, 1]) ➞ "neither"
    
    check([1, 1, 2]) ➞ "neither"

### Notes

  * The last example does NOT count as strictly increasing, since 1-indexed `1` is not strictly greater than the 0-indexed `1`.
  * Input lists have a minimum length of 2.

"""

def check(lst):
  if all([lst[i + 1] > lst[i] for i in range(len(lst) - 1)]):
    return "increasing"
  elif all([lst[i + 1] < lst[i] for i in range(len(lst) - 1)]):
    return "decreasing"
  return "neither"

