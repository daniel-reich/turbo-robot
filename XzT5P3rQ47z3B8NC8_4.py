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

class Condi_Cypher:
​
  def __init__(self, key, shift):
    self.k = ''
    for l8r in key:
      if l8r not in self.k:
        self.k += l8r
    self.shift = shift
    for l8r in 'abcdefghijklmnopqrstuvwxyz':
      if l8r not in self.k:
        self.k += l8r
  
  def encrypt(self, msg):
​
    dic = {n+1:self.k[n] for n in range(26)}
​
    for n in range(26):
      dic[self.k[n]] = n+1
    
    num_msg = []
​
    for l8r in msg:
      try:
        num_msg.append(dic[l8r])
      except KeyError:
        num_msg.append(l8r)
    
    new_num_msg = []
​
    for num in num_msg:
      if isinstance(num, int):
        new_num = num + self.shift
        while new_num > 26:
          new_num -= 26
        new_num_msg.append(new_num)
        self.shift = num
      else:
        new_num_msg.append(num)
    
    new_msg = []
  #  print(new_num_msg)
​
    for num in new_num_msg:
      try:
        new_msg.append(dic[num])
      except KeyError:
        new_msg.append(num)
    
    return ''.join(new_msg)
​
​
def condi_cipher(msg, key, shift):
​
  CC = Condi_Cypher(key, shift)
  return CC.encrypt(msg)

