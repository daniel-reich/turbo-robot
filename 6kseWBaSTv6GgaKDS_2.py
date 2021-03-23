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
  i = len(s)-1
  return checkNext(s,i)
  
def checkNext(s,i):
  a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if s=='':
    return 'A'
  elif s[i]!='Z':
    return s[:i]+a[a.index(s[i])+1]
  else:
    return checkNext(s[:i],i-1)+'A'

