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
    if s == '' :
        return 'A'
    elif s.count('Z') == len(s) :
        return (len(s)+1)*'A'
    else :
        z = 0 # number of z at the end of our string
        while s[::-1][z] == 'Z' : z += 1
        pA, pZ = s[::-1][:z:-1], s[-z-1:] # splitting into 2 parts : constant/changed
        pZ = chr(ord(pZ[0])+1) + (len(pZ)-1)*'A' # changing first value to its next one and Z to As
        return pA + pZ

