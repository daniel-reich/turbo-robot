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
    dic = {
    "numbers" : set(list("0123456789")),
    "lower_case" : set(list("abcdefghijklmnopqrstuvwxyz")),
    "upper_case" : set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")),
    "special_characters" : set(list("!@#$%^&*()-+"))
    }
    
    result = 4 - sum([1 for i in dic if len(dic.get(i) & set(password)) > 0])
    if result + len(password) < 6:
        return 6 - len(password)
    else:
        return result

