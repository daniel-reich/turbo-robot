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
  s = list(item)
  letters = []
  digits = []
  for i in s:
    if i.isdigit():
      digits.append(i)
    else:
      letters.append(i)
      
  return [''.join(letters), int(''.join(digits))]

