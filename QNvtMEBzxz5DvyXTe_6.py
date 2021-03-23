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

def strong_password(pw):
    if len(pw) < 6:
        return 6 - len(pw) 
    else:    
        return [any(x.isdigit() for x in pw),
            any(x in "abcdefghijklmnopqrstuvwxyz" for x in pw),
            any(x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for x in pw),
            any(x in "!@#$%^&*()-+" for x in pw)].count(False)

