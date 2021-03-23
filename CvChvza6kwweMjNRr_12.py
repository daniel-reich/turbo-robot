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
  newlst = []
  check = 0
  for x in item:
    if x in "1234567890":
      newlst.append(item[0:check])
      intifier = item[check:len(item)]
      newlst.append(int(intifier))
      return newlst
    else:
      check+=1
      print(check)

