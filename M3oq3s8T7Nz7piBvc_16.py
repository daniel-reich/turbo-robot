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
  evens = ''
  odds = ''
  mylist = []
  for x in txt:
      mylist.append(x)
  for x in range(0, len(txt), 2):
      evens = evens + mylist[x]
  for x in range(1, len(txt), 2):
      odds = odds + mylist[x]
  return evens + " " + odds

