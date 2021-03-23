"""


In **Mubashir Cipher** , encoding is done by simply replacing paired alphabets
from the provided key.

Create a function that takes a string containing the `message` to be encoded
with a fixed given 2D list of alphabets `key`.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'],
        ['s', 'v'], ['h', 'x'], ['i', 'z'], ['r', 'y'],
        ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
    
    message = "edabit is amazing !"
    
    mubashir_cipher(message) ➞ "uqkgzf zv kckizlb !"

 **Step 1:** Search alphabet in the given key and replace it with **paired
alphabet** :

    e = u
    d = q
    a = k
    b = g
    .
    .
    .
    g = b

 **Step 2:** Keep all characters (including spaces) other than alphabets in
their original positions:

    "uqkgzf zv kckizlb !"

See the below examples for a better understanding:

### Examples

    mubashir_cipher("mubashir is not amazing") ➞ "cegkvxzy zv ljf kckizlb"
    
    mubashir_cipher("%$ &%") ➞ "%$ &%"
    
    mubashir_cipher("evgeny sh is amazing") ➞ "usbulr vx zv kckizlb"

### Notes

N/A

"""

import string
​
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  first = ''.join(x[0] for x in key)
  second = ''.join(x[1] for x in key)
  table = message.maketrans(first, second) 
  table.update(message.maketrans(second, first))
  return message.translate(table)

