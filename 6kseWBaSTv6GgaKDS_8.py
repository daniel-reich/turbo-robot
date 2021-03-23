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

def next_letters(s,mem=1):
  d={chr(65+i):i for i in range(26)}
  rd={d[i]:i for i in d}
  lst=[d[i] for i in s[::-1]] if s!='' else [-1]
  res=[]
  for i in lst:
    res+=[rd[(i+mem)%26]]
    if i+mem>25:mem=(i+mem)//26
    else:mem=0
  if mem!=0:res+=[rd[mem-1]]
  return ''.join(res[::-1])

