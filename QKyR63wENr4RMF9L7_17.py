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
  
  a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
  
  indexes = []
  
  for l8r in txt:
    for n in range(0, 26):
      tl8r = a[n]
      if tl8r == l8r:
        indexes.append(n)
        break
  
  ns = ''
  for n in range(0, len(indexes)):
    index = indexes[n]
    dif = lst[n]
    
    nindex = index + dif
    while nindex >= 26:
      nindex -= 26
    nl8r = a[nindex]
    ns += nl8r
  
  return ns

