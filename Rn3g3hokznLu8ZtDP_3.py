"""


Write a function which increments a string to create a new string.

  *  **If the string ends with a number** , the number should be incremented by `1`.
  *  **If the string doesn't end with a number** , `1` should be **added** to the new string.
  *  **If the number has leading zeros** , the amount of digits **should be considered**.

### Examples

    increment_string("foo") ➞ "foo1"
    
    increment_string("foobar0009") ➞ "foobar0010"
    
    increment_string("foo099") ➞ "foo100"

### Notes

N/A

"""

import re
​
def increment_string(t):
  n = ''.join(re.findall(r'\d*\Z', t)) or '0'
  x = str(int(n)+1)
  r = '0'*(len(n)-len(x)) + x
  return t.replace(n, r) if int(n) else t+'1'

