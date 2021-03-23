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
  temp = list(s)
  temp2 = []
  output = ""
  count = 1
  carry = 1
  for c in temp[::-1]:
    carry = 0
    if(c == 'Z'):
      if(count == 1):
        temp2.insert(0,'A')
        carry = 1
      else:
        temp2.insert(0,c)
        count = 0
    else:
      if(count == 1):
        temp2.insert(0,chr(ord(c)+1))
        count = 0
      else:
        temp2.insert(0,c)
        count = 0
  if carry: temp2.insert(0, 'A')
  for t in temp2:
    output += t
  return output

