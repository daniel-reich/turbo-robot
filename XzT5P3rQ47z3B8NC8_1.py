"""


In **Condi Cipher** , encoding is done by shifting a string of messages in
correspondence with a given key in the plaintext.

Create a function that takes three arguments, `key`, `shift` and `message`,
and returns the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "on.,"
    shift = 10
    key = "cryptogram"
    
    condi_cipher(message, key, shift) ➞ "jx.,"

Step 1: **Remove duplicate alphabets** of the key. **Rearrange alphabets**
from A-Z, such that the keyword appears first, followed by the rest of the
alphabets in the usual order.

    c r y p t o g a m b d e f h i j k l n q s u v w x z

Step 2: Starting from 1, **assign numbers** to the letters:

    1  2  3  4  5  6  7  8  9  10 11 12 13
    c  r  y  p  t  o  g  a  m  b  d  e  f 
    14 15 16 17 18 19 20 21 22 23 24 25 26
    h  i  j  k  l  n  q  s  u  v  w  x  z

Step 3: **Replace each alphabet** of the message with the letter in the
modified key shifter by a constant positive number `shift` (wrapping is
required if the shift is greater than key size):

       'o' = 'j'
    # 'j' is 10 places right to 'o'

Step 4: Use the **position of the previous letter** as the number of places to
move to encode the next plaintext number. If you have just encoded an 'o'
(position 6), and you now want to encode 'n', then you have to move 6 places
to the right from 'n' which brings you to 'x'.

       'n' = 'x'
    # 'x' is 6 places right to 'n'
    # keep other characters in same order
    
    eMessage = "jx.,"

See the below examples for a better understanding:

### Examples

    condi_cipher("on.,", "cryptogam", 10) ➞ "jx.,"
    
    condi_cipher("mubashir", "airforce", 6) ➞ "ugrdtfko"
    
    condi_cipher("matt", "edabit", 2) ➞ "opgk"

### Notes

N/A

"""

def condi_cipher(message, key, shift):
    k, set_k = "", set()
    for c in key:
        if c not in set_k:
            k += c
            set_k.add(c)
    k += "".join(chr(i + 97) for i in range(26) if chr(i + 97) not in set_k)
    res = []
    for i, c in enumerate(message):
        if c.isalpha():
            x = k[(k.index(c) + shift) % 26]
            shift = k.index(c) + 1
        else:
            x = c
        res.append(x)
    return "".join(res)

