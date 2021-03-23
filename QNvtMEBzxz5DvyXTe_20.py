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
   num = 0
   lcase = 0
   ucase = 0
   sc = 0
   count = 5
   numbers = "0123456789"
   lower_case = "abcdefghijklmnopqrstuvwxyz"
   upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   special_characters = "!@#$%^&*()-+"
   if len(password) < 6:
      return 6 - len(password)
   for x in password:
      if x in numbers:
         num += 1
      if x in lower_case:
         lcase += 1
      if  x in upper_case:
         ucase += 1
      if x in special_characters:
         sc += 1
   if num > 0 :
      count -=  1
   if lcase > 0:
      count -= 1
   if ucase > 0 :
     count -=  1
   if sc > 0 :
      count -= 1
   return count -1

