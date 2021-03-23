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

from re import split
def validate_email(t):
  if t == "":
    return False
  t = [y.split(".") for y in t.split("@")]
  if len(t) == 1:
    return False
  return len(t[1]) == 2 and len(t[0]) >= 1 and "" not in t[0]

