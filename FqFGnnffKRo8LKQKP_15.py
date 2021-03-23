"""


 **Mubashir** needs your help to filter out **Simple Numbers** from a given
list.

### Simple Numbers

    89 = 8^1 + 9^2
    135 = 1^1 + 3^2 + 5^3

Create a function to collect these numbers from a given range between `a` and
`b` (both numbers are inclusive).

### Examples

    simple_numbers(1, 10) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    simple_numbers(1, 100) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    
    simple_numbers(90, 100) ➞ []

### Notes

N/A

"""

def is_simple(n):
  return n == sum(int(d)**i for i, d in enumerate(str(n), 1))
​
def simple_numbers(a, b):
  return [n for n in range(a, b+1) if is_simple(n)]
