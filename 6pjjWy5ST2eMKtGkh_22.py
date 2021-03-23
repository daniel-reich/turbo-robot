"""


Write a function that replaces all letters within a specified range with the
hash symbol `#`.

### Examples

    replace("abcdef", "c-e") ➞ "ab###f"
    
    replace("rattle", "r-z") ➞ "#a##le"
    
    replace("microscopic", "i-i") ➞ "m#croscop#c"
    
    replace("", "a-z") ➞ ""

### Notes

  * The range will always be in order, a.k.a. for `m-n`, character `m` will always come before or equal `n`.
  * Strings will be in lower case letters only.
  * Return an empty string if the input is an empty string.

"""

def replace(txt, r):
  mystr = ""
  for i in range (len(txt)):
    if (ord(txt[i])>=ord(r[0]) and ord(txt[i])<=ord(r[2])):
      mystr += "#"
    else:
      mystr += txt[i]
  return mystr

