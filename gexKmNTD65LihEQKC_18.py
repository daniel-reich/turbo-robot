"""


Arun was playing random games with numbers, and he realized that four is a
number whose English reformation (i.e. FOUR, also has four letters). He
noticed an interesting pattern.

Arun starts with a few chosen strings and lands upon a number that has the
same number of letters in it as the magnitude of the number (e.g. Alienware-
Computers has nineteen letters in it, nineteen has eight letters, eight has
five and five has four letters and four again has four letters in it).

So, Alienware-Computers is a super cool string as this word can be converted
into a number which has the same length as it's magnitude when the given
string is written in English.

Arun has a few more strings. Help him figure out if they're _super cool_ or
not.

### Examples

    is_super_cool("A") ➞ True
    # "A" has one letter.
    # One has three letters.
    # Three has five letters.
    # Five has four letters.
    # Four has four letters.
    
    is_super_cool("Nura") ➞ True)
    
    is_super_cool("") ➞ False

### Notes

This challenge is _possible_ without using loops.

"""

def is_super_cool(string):
  return (True if len(string)>0 else False)

