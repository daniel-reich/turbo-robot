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

def polybius(t):
  f=lambda d,v:list(d.keys())[list(d.values()).index(v)]if v!='24'else'I'
  d={y:'%s%s'%(i,j)for i,x in enumerate(['ABCDEFGHIKLMNOPQRSTUVWXYZ'[i:i+5]for i in range(0,25,5)],1)for j,y in enumerate(x,1)}
  d['J']=d['I']
  return' '.join(''.join(f(d,x[i:i+2])for i in range(0,len(x),2))for x in t.split()).lower()if t[:2].isdigit()else' '.join(''.join(d[y]for y in x if y.isalpha())for x in t.upper().split())

