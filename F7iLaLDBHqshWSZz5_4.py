"""


Create a function that takes as a parameter a list of "stringified" numbers
and returns a list of numbers.

Example:

    ["1", "3", "3.6"] ➞ [1, 3, 3.6]

### Examples

    to_number_list(["9.4", "4.2"]) ➞ [9.4, 4.2]
    
    to_number_list(["99", "20"]) ➞ [99, 20]
    
    to_number_list(["9.5", "8.8"]) ➞ [9.5, 8.8]

### Notes

Some inputs are floats.

"""

def to_float_list(lst):
  return [float(x) for x in lst]

