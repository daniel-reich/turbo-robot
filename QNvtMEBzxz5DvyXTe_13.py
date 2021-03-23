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
    special = '!@#$%^&*()-+'
    digit_in, upper_in, lower_in, special_in = 1, 1, 1, 1
    for c in password:
        if c.isdigit():
            digit_in = 0
        elif c.isalpha():
            if c.islower():
                lower_in = 0
            elif c.isupper():
                upper_in = 0
        elif c in special:
            special_in = 0
    add_on = digit_in + upper_in + lower_in + special_in
    return add_on if add_on + len(password) > 5 else 6 - len(password)

