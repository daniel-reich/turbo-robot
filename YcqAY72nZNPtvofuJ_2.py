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
  l = len(lst)
  j = [lst[x+1]-lst[x] for x in range(2)]
  a = (j[1]-j[0])/2
  b = j[0]-3*a
  c = lst[0] - a - b
  return ([int(a*n**2 + b*n + c) for n in range(l+1, 2*l+1)])

