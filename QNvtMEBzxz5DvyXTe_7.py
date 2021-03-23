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
​
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"
​
  # # lists of the above strings
  numbers    = list(numbers)
  lower_case = list(lower_case)
  upper_case = list(upper_case)
  special_characters = list(special_characters)
​
  # print(numbers, "\n", 
  #    lower_case, "\n",
  #    upper_case, "\n",
  #    special_characters)
​
​
  # Criteria Check:
  # ===============
​
  # Preliminary - split the password into a list
  password = list(password)
  # create a unicode lsit as well instead of doing it 
  # all the time in the loops 
​
  count_changes_required = 0  
  
  # 1. The password length must be at least 6.
  if len(password) < 6:
    # print("The password needs to be at least 6 characters long")
    count_changes_required = 6 - len(password)
    return count_changes_required
​
  # 2. The password contains at least one digit.
  # check if all characters in string belong to a range of unicode 
  # values  
  count_digits = 0 
​
  # This could be wrapped into a function 
  for c in password:
    if str(c) in numbers:
      count_digits += 1
​
  if count_digits < 1:
    # print("Password requires at least one digit")
    count_changes_required += 1
​
  # 3. The password contains at least on e lowercase English Character.
  # 97 - 122
  count_letters_lc = 0
  for c in password:
    if c in lower_case:
      count_letters_lc += 1
​
  if count_letters_lc < 1:
    # print("Password requires at least one lower case letter")
    count_changes_required += 1
​
  # 4. The password contains at least on e upperercase English Character.
  # 65 - 90
  count_letters_uc = 0
  for c in password:
    if c in upper_case:
      count_letters_uc += 1
​
  if count_letters_uc < 1:
    # print("Password requires at least one upper case letter")
    count_changes_required += 1
  
​
  # 5. The password contains at least one special character.
  count_special_chars =  0
  for c in password:
    if c in special_characters:
      count_special_chars += 1
​
  if count_special_chars < 1:
    # print("Password requires at least one special digit")
    count_changes_required += 1
​
  return count_changes_required

