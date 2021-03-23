"""


Create a function which returns a list of _booleans_ , from a given number.
Iterating through the number one digit at a time, append `True` if the digit
is 1 and `False` if it is 0.

### Examples

    integer_boolean("100101") ➞ [True, False, False, True, False, True]
    
    integer_boolean("10") ➞ [True, False]
    
    integer_boolean("001") ➞ [False, False, True]

### Notes

Expect numbers with 0 and 1 only.

"""

def integer_boolean(n):
  n.split()
  return list(map(to_bool,n))
  
def to_bool(chr):
  return True if chr == "1" else False

