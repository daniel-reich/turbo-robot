"""


Write a function that, given the `start_of_range` and `end_of_range` values,
returns an array containing all the numbers **inclusive** to that range. See
examples below.

### Examples

    reversible_inclusive_list(1, 5) ➞ [1, 2, 3, 4, 5]
    
    reversible_inclusive_list(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]
    
    reversible_inclusive_list(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    reversible_inclusive_list(24, 17) ➞ [24, 23, 22, 21, 20, 19, 18, 17]

### Notes

  * The sort order of the resulting array is dependent of the input values.
  * All inputs provided in the test scenarios are valid.
  * If `start_of_range` is greater than `end_of_range`, return a **descendingly** sorted array, otherwise, **ascendingly** sorted.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/3ucrYGBkvJwjbFL4G).

"""

def reversible_inclusive_list(start, end):
  if start < end:
    return list(range(start, end + 1))
  elif start > end:
    return list(reversed(list(range(end, start + 1))))
  else:
    return [end]

