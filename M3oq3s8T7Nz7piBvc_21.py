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
​
  Even = ""
  Odd = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Letter = txt[Counter]
    
    if (Counter % 2 == 0):
      Even = Even + Letter
      Counter += 1
    else:
      Odd = Odd + Letter
      Counter += 1
      
  Answer = Even + " " + Odd
  return Answer

