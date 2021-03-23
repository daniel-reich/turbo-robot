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

def strong_password(pwd):
  ns = '0123456789'
  ls = 'abcdefghijklmnopqrstuvwxyz'
  us = ls.upper()
  ss = '!@#$%^&*()-+'
  nx = not any(c in ns for c in pwd)
  lx = not any(c in ls for c in pwd)
  ux = not any(c in us for c in pwd)
  sx = not any(c in ss for c in pwd)
  return max(6-len(pwd), nx+lx+ux+sx)

