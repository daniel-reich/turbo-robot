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

def tweak_letters(txt, lst):
  a=[ord(i) for i in txt]
  b=[x+y for x,y in zip(a,lst)]
  c=[]
  for j in b:
    if j>122:c.append(chr(j-26))
    elif j<97:c.append(chr(j+26))
    else:c.append(chr(j))
  return ''.join(c)

