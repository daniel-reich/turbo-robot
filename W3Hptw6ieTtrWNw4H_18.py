"""


The basic **Polybius Square** is a 5x5 square grid with the letters A-Z
written into the grid. "I" and "J" typically share a slot (as there are 26
letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
The **Bifid** cipher uses the Polybius square but adds a layer of complexity.

Start with a secret message. Remove spaces and punctuation.

    plaintext = "ikilledmufasa"

Encipher the message using the basic Polybius cipher (see my [previous
challenge](https://edabit.com/challenge/2C3gtb4treAFyWJMg) — right click and
select "open in new tab"), but write the numbers in two rows under the
message, like so:

i| k| i| l| l| e| d| m| u| f| a| s| a  
---|---|---|---|---|---|---|---|---|---|---|---|---  
2| 2| 2| 3| 3| 1| 1| 3| 4| 2| 1| 4| 1  
4| 5| 4| 1| 1| 5| 4| 2| 5| 1| 1| 3| 1  
  
Read off the numbers horizontally, in pairs:

    22 23 31 13 42 14 14 54 11 54 25 11 31

Generate the ciphertext by converting these new pairs of numbers into new
letters using the Polybius square.

    ciphertext = "ghlcrddyaykal"

Create a function that takes a plaintext or ciphertext, and returns the
corresponding ciphertext or plaintext.

### Examples

    bifid("I killed Mufasa!") ➞ "ghlcrddyaykal"
    
    bifid("ghlcrddyaykal") ➞ "ikilledmufasa"
    
    bifid("hi") ➞ "go"

### Notes

N/A

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
    row = []
    for c in code:
        r, c = map2[c]
        row.append(r)
        row.append(c)
    L = len(row)
    row1, row2 = row[:L//2], row[L//2:]
    msg = ""
    for i in range(len(row1)):
        r, c = row1[i], row2[i]
        msg += map1[(r,c)]
    return msg
    
def encipher(text):
    row1, row2 = [], []
    for char in text.lower():
        if 'a' <= char <= 'z':
            row, col = map2[char]
            row1.append(row)
            row2.append(col)
    row = row1 + row2
    code = ""
    for i in range(len(row) // 2):
        r, c = row[2*i:2*i+2]
        code += map1[(r, c)]#str(row) + str(col)
    return code
​
def bifid(text):
    if all(['a' <= c <= 'z' for c in text]):
        # it's ciphertext, so decipher:
        return decipher(text)
    else:
        # it's a plain text, so encipher:
        return encipher(text)

