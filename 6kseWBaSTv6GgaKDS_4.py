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

def next_letters(w):
  if w=="": return "A"
  lst=[ord(i)-64 for i in w]
  lst[-1]=lst[-1]+1
  for i in range(-1,-(len(lst)+1),-1):
   if lst[i]>26:
     try:lst[i-1]=lst[i-1]+1
     except:
      lst.insert(i, 0)
      lst[i - 1] = lst[i - 1] + 1
​
  return "".join([chr(i+64) if i <27 else chr((i%26)+64) for i in lst])

