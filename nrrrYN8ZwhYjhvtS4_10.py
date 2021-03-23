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
  s=''
  if type(num)==int and num>=0:
    for x in word:
      if x.lower() in 'aeiou':
        s+=x*(num+1)
      else:
        s+=x
    return s
  else:
    return "invalid"

