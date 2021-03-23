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

def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  k2 = {i[0]:i[1] for i in key}
  for j in key:
    k2[j[1]]=j[0]
  output = ""
  for i in message:
    if i in k2:
      output += k2[i]
    else:
      output += i
  return output

