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
    txt = [i for i in txt]
    for i in range(len(txt)):
        if txt[i-1] == "-" or txt[i-1] == "_":
            txt[i] = txt[i].upper()
    txt = "".join(txt)
    if "_" in txt:
        txt = txt.replace("_","")
    if "-" in txt:
        txt = txt.replace("-","")
    return txt

