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
    integer = txt[-1]
    i = 2
    while txt[-i].isdigit():
      integer = txt[-i] + integer
      i += 1
    i -= 1
    orig_len = len(integer)
    num = int(integer) + 1
    zeros = ""
    if len(str(num)) < orig_len:
      diff = orig_len - len(str(num))
      zeros = '0' * diff
    return txt[:-i] + zeros + str(num)
  else:
    return(txt+'1')

