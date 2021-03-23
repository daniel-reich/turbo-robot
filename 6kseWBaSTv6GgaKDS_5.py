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

import re
​
def next_letters(s):
    if set(s) == {'Z'}:
        return 'A' * (len(s) + 1)
    if 'Z' not in s:
        return s[:-1] + chr(ord(s[-1]) + 1)
    front, mid, back = re.findall('(.*)([^Z])(Z+)$', s)[0]
    return front + chr(ord(mid) + 1) + 'A' * len(back)

