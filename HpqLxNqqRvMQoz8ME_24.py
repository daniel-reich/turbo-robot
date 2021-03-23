"""


Create a function that takes a string and returns a string in which each
character is repeated once.

### Examples

    double_char("String") ➞ "SSttrriinngg"
    
    double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
    
    double_char("1234!_ ") ➞ "11223344!!__  "

### Notes

All test cases contain valid strings. Don't worry about spaces, special
characters or numbers. They're all considered valid characters.

"""

def double_char(txt):
    return ''.join(x+x for x in txt)

