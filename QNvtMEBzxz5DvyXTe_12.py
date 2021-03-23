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

def strong_password(password):
  special_chars = "!@#$%^&*()-+"
  if len(password) < 6:
    length = 6 - len(password)
  else:
    length = 0
  digits = list(filter(lambda x: x.isdigit(),password))
  special = list(filter(lambda x: x in special_chars,password))
  lower = list(filter(lambda x: x.islower(),password))
  upper = list(filter(lambda x: x.isupper(),password))
  
  amount = len(list(filter(lambda x: len(x) == 0, [digits,special,lower,upper])))
  return max(amount,length)

