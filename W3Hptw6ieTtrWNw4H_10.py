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
  a = 'abcdefghiklmnopqrstuvwxyz'
  b = iter(a)
  d1 = {next(b):(r,c) for r in range(1,6) for c in range(1,6)}
  d2 = {v:k for k,v in d1.items()}
  enc = True if ' ' in text else False
  t = str.maketrans('j', 'i')
  text = ''.join(c for c in text.lower().translate(t) if c in a)
  if enc:
    tmp = [d1[c][0] for c in text] + [d1[c][1] for c in text]
    tups = [(tmp[i], tmp[i+1]) for i in range(0, len(tmp), 2)]
  else:
    tmp = [n for c in text for n in d1[c]]
    l2 = len(tmp) // 2
    tups = zip(tmp[:l2], tmp[l2:])
  return  ''.join([d2[tup] for tup in tups])

