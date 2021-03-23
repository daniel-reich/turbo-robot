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
  return 'invalid' if num%1 or num<0 else ''.join(i*(num+1) if i in 'aeiouAEIOU' else i for i in word )

