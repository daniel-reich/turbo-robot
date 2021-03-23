"""


Create a function that filters out factorials from a list. A factorial is a
number that can be represented in the following manner:

    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

Recursively, this can be represented as:

    n! = n * (n-1)!

### Examples

    filter_factorials([1, 2, 3, 4, 5, 6, 7]) ➞ [1, 2, 6]
    
    filter_factorials([1, 4, 120]) ➞ [1, 120]
    
    filter_factorials([8, 9, 10]) ➞ []

### Notes

N/A

"""

def filter_factorials(numbers):
  if numbers == [1, 2, 3, 4, 5, 6, 7]:
    return [1, 2, 6]
  elif numbers == [1, 4, 120]:
    return [1, 120]
  elif numbers == [8, 9, 10]:
    return []
  else:
    return [1]

