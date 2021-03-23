"""


Create a function that determines the minimum number of characters needed to
make a strong password.

A password is considered _strong_ if it satisfies the following criteria:

  * Its length is at least 6.
  * It contains at least one digit.
  * It contains at least one lowercase English character.
  * It contains at least one uppercase English character.
  * It contains at least one special character: `!@#$%^&*()-+`

Types of characters in a form you can paste into your solution:

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

### Examples

    strong_password(“Ed1”) ➞ 3
    
    strong_password(“#Edabit”) ➞ 1
    
    strong_password("W1llth!spass?") ➞ 0

### Notes

Try solving this without RegEx.

"""

import re
def strong_password(s):
  s1="\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\+ [a-z] [A-Z] \d";c=0
  for i in s1.split():
    if re.search(i,s):
      pass
    else:
      c=c+1
  if c+len(s)<6:
    return c+(6-(c+len(s)))
  else:
    return c

