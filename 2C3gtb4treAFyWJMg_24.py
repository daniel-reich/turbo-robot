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

def polybius(text):
    grid = [['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z']]
    rev = {char: (row_idx+1, col_idx+1) for row_idx,row in enumerate(grid) for col_idx, char in enumerate(row)}
    rev.update({'j': rev['i'], ' ': ' '})
    text = text.lower()
    if text[0].isalpha():
        return ''.join(str(num) for char in text if char in rev for num in rev[char])
    return ' '.join(''.join([grid[int(a)-1][int(b)-1] for a,b in zip(chunk[::2],chunk[1::2])]) for chunk in text.split(' '))

