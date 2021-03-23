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
        return txt.split('-')[0] + ''.join(x.capitalize() for x in txt.split('-')[1:])
    else:
        return txt.split('_')[0] + ''.join(x.capitalize() for x in txt.split('_')[1:])

