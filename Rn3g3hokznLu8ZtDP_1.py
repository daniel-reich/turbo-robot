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
  numlst = []
  end = 0
  for i in range(len(txt) - 1, 0, -1):
    try:
      val = int(txt[i])
      numlst.append(str(val))
    except ValueError:
      end = i + 1
      break
  txt = txt[:end]
  numlst.reverse()
  numlen = len(numlst)
  num = str(1 if numlen == 0 else int("".join(numlst)) + 1)
  num = "0" * (numlen - len(num)) + num
  return txt + num

