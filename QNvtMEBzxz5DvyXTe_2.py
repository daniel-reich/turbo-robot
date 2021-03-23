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
  if(len(password)>=6):
    length=True
  else:
    return 6-len(password)
  upper=False
  lower=False
  number=False
  special=False
  total=0
  for i in password:
    if(i in "abcdefghijklmnopqrstuvwxyz"):
      lower=True
    elif(i in "0123456789"):
      number=True
    elif(i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
      upper=True
    elif(i in "!@#$%^&*()-+"):
      special=True
  if(length and upper and lower and number and special):
    return 0
  if(length):
    total+=1
  if(upper):
    total+=1
  if(lower):
    total+=1
  if(number):
    total+=1
  if(special):
    total+=1
  return (5-total)

