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

def bifid(text):
    coords = [str(i) + str(j) for i in range(1, 6) for j in range(1, 6)]
    encrypt = dict(zip('abcdefghiklmnopqrstuvwxyz', coords))
    decrypt = dict(zip(coords, 'abcdefghiklmnopqrstuvwxyz'))
​
    if text[0].isupper():
        text = ''.join(i for i in text.lower() if i.isalpha())
        nums = text.replace('j', 'i').translate(str.maketrans(encrypt))
        new = ''.join(nums[::2] + nums[1::2])
        return ''.join(decrypt[new[i:i+2]] for i in range(0, len(new), 2))
    else:
        nums = text.replace('j', 'i').translate(str.maketrans(encrypt))
        new = (a + b for a, b in zip(nums[:len(nums)//2], nums[len(nums)//2:]))
        return ''.join(decrypt[i] for i in new)

