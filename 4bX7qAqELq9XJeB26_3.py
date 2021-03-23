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
def to_camel_case(t):
  t = '' if t=='' else t.title() if t[0].isupper() else t[0] + t.title()[1:]
  return re.sub(r'[-_]','',t)

