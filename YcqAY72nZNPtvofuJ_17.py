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

def quad_sequence(lst):
  n1,n2,n3 = lst[0], lst[1], lst[2]
  a = (n1 + n3 - 2 * n2)/2
  b = n3 - a - n2
  return [int(a * i**2 + b * i + n2) for i in range(len(lst)-1, 2*len(lst)-1)]
