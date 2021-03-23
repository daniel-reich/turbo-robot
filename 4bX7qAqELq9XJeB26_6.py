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
def to_camel_case(x):
    for i in range(len(x)):
        if x[i]=="_" or x[i]=="-":
            x = x.replace(x[i+1],x[i+1].upper())
    return re.sub(r'[_-]','',x)

