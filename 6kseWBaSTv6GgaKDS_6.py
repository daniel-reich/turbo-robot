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
    if s == "":
        return "A"
    s = [ord(i) for i in s][::-1]
    b, r = 1, ""
    for i in range(len(s)):
        if s[i] + b == 91:
            r = "A" + r
            b = 1
        else:
            r = chr(s[i] + b) + r
            b = 0
    if b == 1:
        r = "A" + r
    return r

