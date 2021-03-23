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
  passed = {"@": '', ".com": '', "name position": '', \
    "email_position": ''}
  pos_at = 0
  pos_dotcom = 0
  answer = True
  for i in range(len(txt)):
    if txt[i] == "@":
      pos_at = i
      passed["@"] = "Passed"
      print("Passed:  @")
  for i in range(len(txt) - 3):
    if txt[i] == '.' and txt[i : i+ 4] == '.com':
      pos_dotcom = i
      passed[".com"] = 'Passed'
      print("Passed:  .com")
  if pos_at < pos_dotcom and (pos_dotcom -  pos_at) > 1:
    passed["email_position"] = "Passed"
    print('Passed: gmail.com')
  if pos_at != 0 and pos_dotcom != 0:
    print(txt[:pos_at])
    passed["name position"] = 'Passed'
    print("Passed:  name")
  print(passed)
  for item in passed:
    if passed[item] == '':
      answer = False
  return(answer)

