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
  tf = [False,False,False,False]
  ret = 4
  special_characters = "!@#$%^&*()-+"
  for x in password:
    if(x.isdigit()):
      tf[0] = True 
    if(x.islower()):
      tf[1] = True
    if(x.isupper()):
      tf[2] = True
    if(x in special_characters):
      tf[3] = True
  for y in tf:
    if(y == True):
      ret -= 1
  if(len(password) < 6):
    ret = 6 - len(password)
  return ret

