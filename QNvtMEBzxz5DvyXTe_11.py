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
    def a(password):
        if any(i.isdigit() for i in password):
            return 0
        else:
            return 1    
    def b(password):
        if any(i.islower() for i in password):
            return 0
        else:
            return 1   
    def c(password):
        if any(i.isupper() for i in password):
            return 0
        else:
            return 1    
    def d(password):
        if any(i in "!@#$%^&*()-+" for i in password):
            return 0
        else:
            return 1    
    j=a(password)+b(password)+c(password)+d(password)
    if len (password)>=6 and j==0:
        return 0
    
    if len (password)>=6 and j!=0:
        return j
    
    else:
        return 6-len(password)

