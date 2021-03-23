"""


You have a list of item codes with the following format: `"[letters][digits]"`

Create a function that splits these strings into their alphabetic and numeric
parts.

### Examples

    split_code("TEWA8392") ➞ ["TEWA", 8392]
    
    split_code("MMU778") ➞ ["MMU", 778]
    
    split_code("SRPE5532") ➞ ["SRPE", 5532]

### Notes

N/A

"""

def split_code(item):
  dg_tmp = ''
  alpha_tmp = ''
  for lt in item:
    if lt.isdigit():
      dg_tmp += lt
    elif lt.isalpha():
      alpha_tmp += lt
  return [alpha_tmp, int(dg_tmp)]

