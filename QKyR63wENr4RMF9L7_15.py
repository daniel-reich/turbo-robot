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

def tweak_letters(string, steps):
  return "".join([rotate(letter , value) for letter , value in zip(string,steps)]);
  
def rotate(letter , step):
  return "a" if (letter,step) == ("z" , 1)  else "z" if (letter , step) == ("a" ,-1) else chr(ord(letter) + step)

