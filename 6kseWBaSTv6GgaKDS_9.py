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
    if s == "":
        return 'A'
    if s[-1] != 'Z':
        return s[:-1] + chr(ord(s[-1]) + 1)
    s = s[:-1] + 'A'
    for idx in range(len(s) - 2, -1, -1):
        if s[idx] != 'Z':
            return s[:idx] + chr(ord(s[idx]) + 1) + s[idx+1:]
        s = s[:idx] + 'A' + s[idx+1:]
    return 'A' + s

