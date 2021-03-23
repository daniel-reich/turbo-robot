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

get_char = lambda r,c: chr(ord('a') + r*5 + c + (1 if r > 1 or (r == 1 and c > 3) else 0))
get_rc = lambda ch: divmod(ord(ch) - ord('a') - (1 if ch > 'i' else 0), 5)
​
def bifid(text):
    if ' ' in text:
        rc = [[],[]]
        for r,c in [get_rc(c) for c in text.lower() if c.isalpha()]:
            rc[0].append(r)
            rc[1].append(c)
        crc, res = rc[0]+rc[1], ''
        return ''.join(get_char(r,c) for r,c in [crc[i:i+2] for i in range(0, len(crc), 2)])
    else:
        crc, tl = [], len(text)
        for r,c in [get_rc(c) for c in text]:
            crc += [r, c]
        return ''.join(get_char(r,c) for r,c in zip(crc[0:tl], crc[tl:]))

