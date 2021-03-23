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

#bad code, got tired
def strong_password(password):
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"
​
  startnum = 5
​
  for i in numbers:
    if i in password:
      print("numbers: Check!")
      startnum = startnum - 1
      break
​
​
  for i in lower_case:
    if i in password:
      print("lower_case: Check!")
      startnum = startnum - 1
      break
​
​
  for i in upper_case:
    if i in password:
      print("upper_case: Check!")
      startnum = startnum - 1
      break
​
​
  for i in special_characters:
    if i in password:
      print("special_characters: Check!")
      startnum = startnum - 1
      break
​
  if len(password) >= 4:
    startnum = startnum - 1
    print("length: Suffices!")
  else:
      print("length: Doesn't suffice!")
  
  if len(password) == 1: 
    return 5
  elif len(password) == 2:
    return 4
​
  return startnum

