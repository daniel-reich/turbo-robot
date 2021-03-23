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
  def factorial(n, i=1):
    return n == 1 or (n%i==0 and factorial(n//i, i+1))
  return [n for n in numbers if factorial(n)]

