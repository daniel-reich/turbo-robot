"""


Write a function that, given the `start` and `end` values, returns an array
containing all the numbers **inclusive** to that range. See examples below.

### Examples

    reversible_inclusive_list(1, 5) ➞ [1, 2, 3, 4, 5]
    
    reversible_inclusive_list(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]
    
    reversible_inclusive_list(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    reversible_inclusive_list(24, 17) ➞ [24, 23, 22, 21, 20, 19, 18, 17]

### Notes

  * The sort order of the resulting array is dependent of the input values.
  * All inputs provided in the test scenarios are valid.
  * If `start` is greater than `end`, return a **descendingly** sorted array, otherwise, **ascendingly** sorted.
  * You are expected to solve this challenge via a **recursive** approach.
  * An iterative version of this challenge can be found via this [link](https://edabit.com/challenge/zW9JME7XNew4tgCCE).

"""

def reversible_inclusive_list(start, end, rev=None):
    if rev is None:
        if start > end:
            rev = True
            start, end = end, start
        else:
            rev = False       
    if start >= end:
        return [start]
    if rev:
        return reversible_inclusive_list(start+1, end, rev) + [start]
    else:
        return [start] + reversible_inclusive_list(start+1, end, rev)

