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
  nums = list("123456789")
  letters = []
  digits = []
  for i in range(len(item)):
    if item[i] in nums:
      digits.append(item[i])
    else:
      letters.append(item[i])
  val = "".join(digits)
  val = int(val)
  return ["".join(letters), val]

