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

def increment_string(s):
    a = ""
    s_yedek = s
    while s_yedek[-1].isdigit():
      a = s_yedek[-1]+a
      s_yedek = s_yedek[:-1]
    if a != "":
      sayi = int(a)+1
    else:
      sayi = 1
    if len(a) >= len(str(sayi)):
      s = s[:-(len(str(sayi)))]+str(sayi)
    elif a == "":
      s = s + str(sayi)
    else:
      s = s[:len(a)]+str(sayi)
    return s

