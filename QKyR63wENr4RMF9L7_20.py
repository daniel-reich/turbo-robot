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

def fix(num):
  n = num + 26 if num < 97 else num - 26 if num > 122 else num
  return chr(n)
  
def tweak_letters(txt, lst):
  return ''.join(fix(ord(ch) + i) for ch, i in zip(txt,lst))

