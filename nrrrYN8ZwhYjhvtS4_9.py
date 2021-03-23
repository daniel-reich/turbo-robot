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
 if type(num) is int and num>0:
  listt=[letter for letter in word]
  return ''.join(list(map(lambda x:x*(num+1) if x in 'aeiuoAEIOU' else x, listt)))
 elif num==0:
   return word
 else:
   return 'invalid'

