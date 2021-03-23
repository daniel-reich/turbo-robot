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

cipher = {"a" : "k", "b" : "g", "c" : "m", "d" : "q", "e" : "u", "f" : "t",
        "g" : "b", "h" : "x", "i" : "z", "j" : "o", "k" : "a", "l" : "n",
        "m" : "c", "n" : "l", "o" : "j", "p" : "w", "q" : "d", "r" : "y",
        "s": "v", "t": "f", "u": "e", "v": "s", "w": "p", "x": "h",
        "y": "r", "z": "i"}
​
def mubashir_cipher(message):
    message = message.lower()
    new_message = ""
    for letter in message:
        if letter in cipher:
            new_message += cipher[letter]
        else:
            new_message += letter
    return new_message

