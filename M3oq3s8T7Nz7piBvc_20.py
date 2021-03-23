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
  i = 1
  even =''
  odd =''
  for _ in txt:
    if i % 2 ==0:
      even += txt[i-1]
    else:
      odd += txt[i-1]
    i += 1
  rslt = odd+" "+even
  return rslt

