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
  if not txt[-1].isnumeric(): return txt + '1'
  i = 0
  for i in range(1, len(txt) + 1):
    if not txt[-i:].isnumeric(): break
  i -= 1
  string = txt[:-i]
  number = str(int(txt[-i:]) + 1)
  return string + '0' * max(len(txt) - len(number) - len(string), 0) + number

