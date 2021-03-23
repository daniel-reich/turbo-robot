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
  lis=[]
  if '-' in txt:
    lis = txt.split('-')
  elif '_' in txt:
    lis = txt.split('_')
  for i in range(1,len(lis)):
    if lis[i][0].islower():
      lis[i] = lis[i].capitalize()
  return "".join(lis)

