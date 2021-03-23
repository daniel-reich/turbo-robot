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

import re;
def split_code(item):
  alphabets = re.findall(r'[a-zA-Z]+',item);
  digits = re.findall(r'\d+',item);
  return alphabets + [int(digits[0])];

