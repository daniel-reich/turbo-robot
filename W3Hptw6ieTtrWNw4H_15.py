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

key = (
  ('a','b','c','d','e'),
  ('f','g','h','i','k'),
  ('l','m','n','o','p'),
  ('q','r','s','t','u'),
  ('v','w','x','y','z'))
​
def bifid(txt):
  if all(ch.islower() for ch in txt):
    lst = []
    for ch in txt:
      x, y = get_index(ch)
      lst.append(x)
      lst.append(y)
    mid = len(lst)//2
    top, bottom = lst[:mid], lst[mid:]
    lst = [(top[i],bottom[i]) for i in range(len(top))]
    return ''.join(get_letter(i) for i in lst)
    
  else:
    lst = [get_index(ch) for ch in txt.lower() if ch.isalpha()]
    lst = [i[0] for i in lst] + [i[1] for i in lst]
    return ''.join(get_letter((lst[i],lst[i+1])) for i in range(0,len(lst)-1,2))
  
def get_index(c):
  global key
  for i, x in enumerate(key):
    if c in x:
      return i,x.index(c)
​
def get_letter(t):
  global key
  r, c = t
  return key[r][c]

