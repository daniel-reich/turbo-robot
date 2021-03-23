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
  if len(s) == 0:
    return "A"
  pos = len(s) - 1
  end = False
  erg = []
  while pos >= 0:
    if not end:
      if s[pos] != "Z":
        neu = chr(ord(s[pos] ) + 1)
        erg.append(neu)
        end = True
      elif pos == 0:
        erg.append("AA")
        end = False
      else:
        erg.append("A")
    else:
      erg.append(s[pos])
    pos -= 1
  erg.reverse()
  return ''.join(erg)

