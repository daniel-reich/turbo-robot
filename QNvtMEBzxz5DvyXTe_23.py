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

# without regex
def strong_password(password):
    up = low = digit = special = False
​
    for letter in password:
        if letter.isupper():
            up = True
        elif letter.islower():
            low = True
        elif letter.isdigit():
            digit = True
        elif letter in "!@#$%^&*()-+":
            special = True
​
    missing_criteria = 4 - sum((up, low, digit, special))
    new_size = len(password) + missing_criteria
​
    if new_size >= 6:
        return missing_criteria
    return 6 - new_size + missing_criteria

