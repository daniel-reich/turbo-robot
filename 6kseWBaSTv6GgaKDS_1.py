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

from re import search, findall
​
def next_letters(x):
  if not len(x): return 'A'
  if search(r'Z\Z', x) is None:
    return x[:-1] + chr(ord(x[-1])+1)
  else:
    r = findall(r'[A-Y]?Z+\Z', x)[0]
    t = ''.join('A' if a == 'Z' else chr(ord(a)+1) for a in r)
    return t + 'A' if len(t) == len(x) else x[:-len(r)] + t

