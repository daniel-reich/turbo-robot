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
  if not s: return "A"
  a = ord('A')
  z = ord('Z')
​
  s = [ord(x) for x in s]
​
  s[-1] += 1
  
  while z + 1 in s:
    if s[0] == z + 1: #add location in front
      s[0] = a
      s = [a] + s
​
    for i in range(len(s)):
      if s[-i] == z + 1: #overflow to prev digits
        s[-i] = a
        s[-i-1] += 1
  
  s = [chr(x) for x in s]
  
  return ''.join(s)

