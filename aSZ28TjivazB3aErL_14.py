"""


Check if the given string consists of **only letters and spaces** and if every
letter is in **lower case**.

### Examples

    letters_only("PYTHON") ➞ False
    
    letters_only("python") ➞ True
    
    letters_only("12321313") ➞ False
    
    letters_only("i have spaces") ➞ True
    
    letters_only("i have numbers(1-10)") ➞ False
    
    letters_only("") ➞ False

### Notes

  * Empty arguments will always return `False`.
  * Input values will be mixed _(symbols, letters, numbers)_.

"""

import string
def letters_only(s):
  if s == '':
    return False
  else:
    digits = string.digits
    punctuation = string.punctuation
    uppercase = string.ascii_uppercase
    for eachdigit in digits:
      if eachdigit in s:
        return False
    for eachsymbol in punctuation:
      if eachsymbol in s:
        return False
    for eachletter in uppercase:
      if eachletter in s:
        return False
    return True

