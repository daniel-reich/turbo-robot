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

def strong_password(p):
  n = "0123456789"
  l = "abcdefghijklmnopqrstuvwxyz"
  u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  s = "!@#$%^&*()-+"
  no_n = not [0 for i in p if i in n]
  no_l = not [0 for i in p if i in l]
  no_u = not [0 for i in p if i in u]
  no_s = not [0 for i in p if i in s]
  return max(no_n + no_l + no_u + no_s, 6 - len(p))

