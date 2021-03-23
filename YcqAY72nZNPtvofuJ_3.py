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
  a = 0
  b = 0
  c = 0
  constant = lst[0]
  first_difference = lst[1] - lst[0] 
  second_difference = (lst[2]-lst[1])-(first_difference)
  a = second_difference/2
  b = first_difference - 3*a
  c = constant - a - b
  for x in range (len(lst)+1, len(lst)*2+1):
    total = 0
    total = a*(x**2) + b*x + c
    lst[x - len(lst)-1] = total
  return(lst)

