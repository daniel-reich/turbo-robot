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
  if '-' in txt:
    lst = txt.split('-')
    return ''.join([lst[i].title() if i!=0 else lst[i] for i in range(len(lst))])
  elif '_' in txt:
    lst = txt.split('_')
    return ''.join([lst[i].title() if i!=0 else lst[i] for i in range(len(lst))])
  else:
    return ''

