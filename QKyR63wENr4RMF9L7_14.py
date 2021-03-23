"""


Create a function that tweaks letters by one forward (+1) or backwards (-1)
according to a list.

### Examples

    tweak_letters("apple", [0, 1, -1, 0, -1]) ➞ "aqold"
    # "p" + 1 => "q"; "p" - 1 => "o"; "e" - 1 => "d"
    
    tweak_letters("many", [0, 0, 0, -1]) ➞ "manx"
    
    tweak_letters("rhino", [1, 1, 1, 1, 1]) ➞ "sijop"

### Notes

Don't worry about capital letters.

"""

def tweak_letters(word,lst):
 newlis= [j+k for j,k in zip(lst,[ord(i) for i in word])]
 for n,i in enumerate(newlis):
  if i==123:
   newlis[n]=97
  elif i==96:
   newlis[n]=122
 return "".join([chr(i) for i in newlis])

