"""


Create a function that converts dash/underscore delimited words into camel
casing. The first word within the output should be capitalized only if the
original word was capitalized.

### Examples

    to_camel_case("A-B-C") ➞ "ABC"
    
    to_camel_case("the-stealth-warrior") ➞ "theStealthWarrior"
    
    to_camel_case("The_Stealth_Warrior") ➞ "TheStealthWarrior"

### Notes

An empty string as input `""` should return an empty string.

"""

import re
def to_camel_case(txt):
  if not txt:
    return ''
  words = re.findall(r'[A-Za-z]+', txt)
  if words[0][0] == words[0][0].upper():
    return ''.join([word.capitalize() for word in words])
  else:
    return words[0] + ''.join([word.capitalize() for word in words[1:]])

