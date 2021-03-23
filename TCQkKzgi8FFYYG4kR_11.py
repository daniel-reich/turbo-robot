"""


Create a function that takes a string of words (or just one word) and converts
each word from camelCase to snake_case.

### Examples

    camel_to_snake("magicCarrots") ➞ "magic_carrots"
    
    camel_to_snake("greatApples for aSmellyRhino") ➞ "great_apples for a_smelly_rhino"
    
    camel_to_snake("thatsGreat") ➞ "thats_great"

### Notes

You won't get more than two capitals in a row (e.g. `"DIYFoods"` is not
given).

"""

def camel_to_snake(s):
    for char in s:
        if char.isupper():
            s = s.replace(char, ('_'+char.lower()))
    return s

