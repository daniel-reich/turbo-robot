"""


Create a function that follows the "ABACABADABACABA" rule up to a certain
letter.

The _abacabadabacaba_ pattern is where you start with the first letter (a),
and with each new letter, you add the letter in the middle and the others at
the start and end.

For instance:

    A ➞ **A**
    B ➞ A**B**A
    C ➞ ABA**C**ABA
    D ➞ ABACABA**D**ABACABA
    E ➞ ABACABADABACABA**E**ABACABADABACABA
    F ➞ ABACABADABACABAEABACABADABACABA**F**ABACABADABACABAEABACABADABACABA
    
    # And so on ...

### Examples

    ABA("A") ➞ "A"
    
    ABA("B") ➞ "ABA"
    
    ABA("E") ➞ "ABACABADABACABAEABACABADABACABA"

### Notes

N/A

"""

def ABA(s):
  left = ''
  right = ''
  middle = ''
  for x in range(65, ord(s)+1):
    left = left+middle+right
    right = left
    middle = chr(x)
  return left + middle + right

