"""


Create a function that takes a "base number" as an argument. This function
should return another function which takes a new argument, and returns the sum
of the "base number" and the new argument.

Please check the examples below for a clearer representation of the behavior
expected.

### Examples

    # Calling make_plus_function(5) returns a new function that takes an input,
    # and returns the result when adding 5 to it.
    
    plus_five = make_plus_function(5)
    
    plus_five(2) ➞ 7
    
    plus_five(-8) ➞ -3
    # Calling make_plus_function(10) returns a new function that takes an input,
    # and returns the result when adding 10 to it.
    
    plus_ten = make_plus_function(10)
    
    plus_ten(0) ➞ 10
    
    plus_ten(188) ➞ 198
    
    plus_five(plus_ten(0)) ➞ 15

### Notes

All inputs will be valid numbers.

"""

def make_plus_function(base_num):
  return lambda new_num: base_num + new_num

