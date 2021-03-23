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

def to_camel_case(t):
  if t == '': return ''
  j = [i for i in t if not i.isalpha()][0]
  t = t.split(j)
  s = t[0] + ''.join(i.title() for i in t[1:])
  return [s[0].upper()+s[1:], s][s[0].islower()]

