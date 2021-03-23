"""


Write a function that receives a list of _x_ integers and returns a list of
_x_ integers in the Nth term of a quadratic number sequence (where _x_ is the
length of the incoming list). Your function should return the continuation of
the quadratic sequence of the length equal to the length of the given list.

### Examples

    quad_sequence([48, 65, 84]) ➞ [105, 128, 153]
    
    quad_sequence([0, 1, 6, 15, 28]) ➞ [45, 66, 91, 120, 153]
    
    quad_sequence([9, 20, 33, 48]) ➞ [65, 84, 105, 128]

### Notes

Both positive and negative numbers are included in the test cases.

"""

def second_difference(n):
  x, y, z = n[:3]
  return (z-y) - (y-x)
​
def quad_sequence(lst):
  a = second_difference(lst) / 2
  b = (lst[1] - a*(2**2)) - (lst[0] - a*(1**2))
  c = (lst[0] - a*(1**2)) - b
  y = []
  print(a, b, c)
  for i in range(len(lst)+1, len(lst)+len(lst)+1):
    r = (a*(i**2)) + (b*i) + c
    y.append(int(r))
  return y

