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

def strong_password(passwd):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    length = len(passwd)
    digit_flag = 0
    lower_flag = 0
    upper_flag = 0
    special_flag = 0
    for e in passwd:
        if e in numbers:
            digit_flag = 1
        elif e in lower_case:
            lower_flag = 1
        elif e in upper_case:
            upper_flag = 1
        elif e in special_characters:
            special_flag = 1
    total_flags = digit_flag+lower_flag+upper_flag+special_flag
    more_flags = 4 -total_flags
    if more_flags + length >=6:
        num_char_needed = more_flags
    else:
        num_char_needed = more_flags + (6 - (more_flags + length))
    
    return num_char_needed

