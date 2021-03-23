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

from math import floor
import string
def polybius(text):
    # Anonymous Functions
    get_row = lambda idx, width=5: str(1+floor(idx/width))
    get_column = lambda idx,width=5: str(1+idx % 5)
​
    # Create cypher dictionary
    cypher = {}
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
​
    for idx,letter in enumerate(letters):
        if idx > 8:
            idx -= 1  # Down shift to account for I/J sharing
        if letter != 'j':
            row = get_row(idx)
            col = get_column(idx)
            rc = int(row+col)
            cypher[letter] = rc
            cypher[rc] = letter
        else:
            row = get_row(8) # letter i is index 8
            col = get_column(8)
            rc = int(row+col)
            cypher[letter] = rc
            cypher[rc] = 'i'
​
        
​
​
    # Determine if message x is encrypted already
    try:
        _ = int(text.split()[0])
        encrypted = True
    except ValueError:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        encrypted = False
​
​
    if encrypted:
        result = ''
        for term in text.split(' '):
            word = ''
            for i in range(int(len(term)/2)):
                key = int(term[i*2:i*2+2])
                word += cypher[key]
            result += word
            result += ' '
    else:
        result = ''
        for word in text.split(' '):
            term = ''
            for letter in word:
                term += str(cypher[letter])
            result += '{} '.format(term)
​
​
    return result[:-1]

