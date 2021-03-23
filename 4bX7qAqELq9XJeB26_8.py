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
  camel = ''
  i = 0
  while i < len(txt):
    if txt[i] == '-' or txt[i] == '_':
      camel += txt[i+1].upper()
      i += 2
    else:
      camel += txt[i]
      i += 1
  return camel

