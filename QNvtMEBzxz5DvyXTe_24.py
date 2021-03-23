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
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"
  n = 0
  
  n = n+1 if not contains(password,numbers) else n
  n = n+1 if not contains(password,lower_case) else n
  n = n+1 if not contains(password,upper_case) else n
  n = n+1 if not contains(password,special_characters) else n
  
  if len(password)+n < 6:
    n = 6-len(password)
    
  return n
  
def contains(password, container):
  for p in password:
    if p in container: return True
  return False

