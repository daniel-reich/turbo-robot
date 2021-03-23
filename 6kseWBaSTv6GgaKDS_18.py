"""


Create a function which returns the next letters alphabetically in a given
string. If the last letter is a "Z", change the rest of the letters
accordingly.

### Examples

    next_letters("A") ➞ "B"
    
    next_letters("ABC") ➞ "ABD"
    
    next_letters("Z") ➞ "AA"
    
    next_letters("CAZ") ➞ "CBA"
    
    next_letters("") ➞ "A"

### Notes

  * Tests will all be in CAPITALS.
  * Empty inputs should return a capital "A" (as if it were in letter position 0!).
  * Think about the letter "Z" like the number 9 and how it carries over to increment the next letter/digit over.

"""

def next_letters(s):
    res, add_on = '', 1
    for c in s[::-1]:
        res += chr((ord(c) - 65 + add_on) % 26 + 65)
        add_on = 1 if c == 'Z' and add_on == 1 else 0
    if add_on == 1:
        res += 'A'
    return res[::-1]

