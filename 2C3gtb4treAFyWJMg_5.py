"""


The **Polybius Square** cipher is a simple substitution cipher that makes use
of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and
"J" typically sharing a slot (as there are 26 letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
To encipher a message, each letter is merely replaced by its row and column
numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns
the corresponding ciphertext or plaintext.

### Examples

    polybius("Hi") ➞ "2324"
    
    polybius("2324  4423154215") ➞ "hi there"
    
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

### Notes

  * As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
  * Any charactor other than letters and spaces should be dropped from the cypher.

"""

import re
​
def polybius(txt):
  txt = re.sub('[^\w\s]', '', re.sub('j', 'i', txt.lower()))
  
  return re.sub('\d\d', lambda x: decipher(x.group(0)), txt) \
    if txt[0].isdigit() else \
      re.sub('\w', lambda x: encipher(x.group(0)), txt)
      
def decipher(num):
  r, c = map(int, num)
  return chr(ord('a')+(r-1)*5+(c-1)+(num > '24'))
  
def encipher(ch):
  v = 'abcdefghiklmnopqrstuvwxyz'.index(ch)
  return '{}{}'.format(1+v//5, 1+v%5)

