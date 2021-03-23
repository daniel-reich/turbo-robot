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

def next_letters(text):
    newnbrs = []
    inc = 1
    for nbr in list(map (lambda x: ord(x),text.upper()[::-1])):
        newnbr =  nbr + inc
        inc = 0
        if  newnbr > ord("Z"):
            newnbr = ord("A")
            inc = 1
        newnbrs.append(newnbr)
    if inc == 1:
        newnbrs.append(ord("A"))
   
    return "".join(list(map (lambda x: chr(x),newnbrs)))[::-1]
