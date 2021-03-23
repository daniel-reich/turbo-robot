"""


Create a function that accepts a string, checks if it's a valid email address
and returns either `True` or `False`, depending on the evaluation.

  * The string must contain an `@` character.
  * The string must contain a `.` character.
  * The `@` must have at least one character in front of it.
    * e.g. `"e@edabit.com"` is valid while `"@edabit.com"` is invalid.
  * The `.` and the `@` must be in the appropriate places.
    * e.g. `"hello.email@com"` is invalid while `"john.smith@email.com"` is valid.

If the string passes these tests, it's considered a valid email address.

### Examples

    validate_email("@gmail.com") ➞ False
    
    validate_email("hello.gmail@com") ➞ False
    
    validate_email("gmail") ➞ False
    
    validate_email("hello@gmail") ➞ False
    
    validate_email("hello@edabit.com") ➞ True

### Notes

  * Check the **Tests** tab to see exactly what's being evaluated.
  * You can solve this challenge with RegEx, but it's intended to be solved with logic.
  * Solutions using RegEx will be accepted but frowned upon :(

"""

def validate_email(txt):
 if '@' in txt and '@' != txt[0] and '@' != txt[-1] and txt.count('@') == 1:
  i = txt.split("@")
  if i[0] != '.':
   if '.' in i[1] and i[1][0] != '.' and i[1][-1] != '.' :
    return True
   else:
    return False
  else:
   return False
 else:
  return False

