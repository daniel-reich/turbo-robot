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
  factorial = lambda x: 1 if x == 1 else x * factorial(x-1)
  i = 1
  ans = []
  while factorial(i) <= max(numbers):
    if factorial(i) in numbers: ans.append(factorial(i))
    i += 1
  return ans

