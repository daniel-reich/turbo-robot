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
  alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  index_s = alphabets.index(s)
  n = ''
  u = ''
  if s == 'A':
    return s
  else:
    for i in range(index_s+1):
      if alphabets[i] == 'A':
        n = 'A'
      else:
        u = n[:]
        n = n[:] + alphabets[i] + u
    return n

