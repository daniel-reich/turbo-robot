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

import string 
​
def ABA(s):
  ans = ''
  t = list(string.ascii_uppercase)
  for i in t[0:t.index(s) + 1]:
    ans = ans + i + ans
  return ans

