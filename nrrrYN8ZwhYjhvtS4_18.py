"""


Create a function that takes a `word` and extends all vowels by a number
`num`.

### Examples

    extend_vowels("Hello", 5) ➞ "Heeeeeelloooooo"
    
    extend_vowels("Edabit", 3) ➞ "EEEEdaaaabiiiit"
    
    extend_vowels("Extend", 0) ➞ "Extend"

### Notes

Return `"invalid"` if `num` isn't `0` or a positive integer.

"""

def extend_vowels(word, num):
  s=""
  l=["a","e","i","o","u","A","E","I","O","U"]
  if num==0:
    return word
  elif num%1==0 and num>0:
    for i in word:
      if i in l:
        s=s+i*(num+1)
      else:
        s=s+i
    return s
  else:
    return "invalid"

