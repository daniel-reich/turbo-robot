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
    if not s:
        return 'A'
    else:
        if not s[-1]=='Z':
            return s[0:-1]+chr(ord(s[-1])+1)
        else:
            i=len(s)
            while(i>0):
                if s[i-1]=='Z':
                    i=i-1
                else:
                    break
            if i==0:
                return 'A'*(len(s)+1)
            else:
                return s[0:i-1]+chr(ord(s[i-1])+1)+'A'*(len(s)-i)

