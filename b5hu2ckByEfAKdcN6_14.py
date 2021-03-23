"""


Write a function that takes an integer `i` and returns an integer with the
integer backwards followed by the original integer.

To illustrate:

    123

We reverse `123` to get `321` and then add `123` to the end, resulting in
`321123`.

### Examples

    reverse_and_not(123) ➞ 321123
    
    reverse_and_not(152) ➞ 251152
    
    reverse_and_not(123456789) ➞ 987654321123456789

### Notes

`i` is a non-negative integer.

"""

def reverse_and_not(i):
  str1 = str(i)
  str1length = len(str1)
  str2 = str1[str1length::-1]
  i2 = int(str2+str1)
  return i2

