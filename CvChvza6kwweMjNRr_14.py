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
  l=list()
  n=''
  for i in range(len(item)):
    if item[i] in '0123456789':
      n=item[i:]
      break
    else:
      l.append(item[i])
  return [''.join(l),int(n)]

