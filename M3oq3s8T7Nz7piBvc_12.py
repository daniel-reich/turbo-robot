"""


Given a one word lowercase string `txt`, return another string such that even-
indexed and odd-indexed characters are grouped and groups are space-separated.

### Examples

    even_odd_string("mubashir") ➞ "mbsi uahr"
    # Letters at even indexes = "mbsi"
    # Letters at odd indexes = "uahr"
    # Join both strings with a space
    
    even_odd_string("edabit") ➞ "eai dbt"
    
    even_odd_string("airforce") ➞ "aroc ifre"

### Notes

There will be no space in the given string.

"""

def even_odd_string(txt):
 txt1 = ''
 txt2 = ''
 for i,x in enumerate(txt):
  if i % 2 == 0:
    txt1 += txt[i]
  else:
    txt2 += txt[i]
 return txt1 + ' ' + txt2

