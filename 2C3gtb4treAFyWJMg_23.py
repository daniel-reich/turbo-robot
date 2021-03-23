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

map1 = {}
for a in range(97, 123):
    b = a if a <= 105 else a - 1
    row, col = 1 + (b - 97) // 5, 1 + (b - 97) % 5
    map1[(row, col)] = chr(a)
map1[(2, 4)]= 'i'
map2 = {value: key for key, value in map1.items()}
map2['j'] = (2, 4)
​
def decipher(code):
    msg = ""
    idx = 0
    while idx < len(code):
        if code[idx] == ' ':
            msg += ' '
            idx += 1
        else:
            row, col = int(code[idx]), int(code[idx+1])
            msg += map1[(row, col)]
            idx += 2
    return msg.replace('j', 'i')
    
def encipher(text):
    code = ""
    for char in text.lower():
        if char == ' ':
            code += char
        elif 'a' <= char <= 'z':
            row, col = map2[char]
            code += str(row) + str(col)
    return code
​
def polybius(text):
    try:
        k = int(text.replace(' ', ''))
        # it's pure numbers, so decipher:
        return decipher(text)
    except ValueError:
        # it's a text, so encipher:
        return encipher(text)

