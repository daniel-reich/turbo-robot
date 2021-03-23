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
  if txt[-1].isdigit():
    str_alpha = ''.join([x for x in txt if not x.isdigit()])
    str_num = str(int(txt[-(len(txt)-len(str_alpha)):]) + 1)
    while len(txt)-len(str_alpha)-len(str_num):
      str_num = '0' + str_num
    return str_alpha + str_num
  else:
    return txt + '1'

