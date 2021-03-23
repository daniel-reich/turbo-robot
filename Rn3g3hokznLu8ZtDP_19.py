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

def increment_string(txt):
  if not any(x.isnumeric() for x in txt): return txt+'1'
  import re
  m = re.search(r'\d+$', txt)
  l = "%0" + str(len(m.group())) + 'd'
  return txt.split(m.group())[0] + (l % (int(m.group())+1))

