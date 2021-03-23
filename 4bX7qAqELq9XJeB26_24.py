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

def to_camel_case(txt):
  txt_mod = txt.replace('-', '_').split('_')
  if len(txt_mod) <= 1:
    return ''.join(txt_mod)
  return ''.join(txt_mod[0]) + ''.join([i.capitalize() for i in txt_mod[1:]])

