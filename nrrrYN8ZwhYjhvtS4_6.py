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
  if num<0 or isinstance(num,float): return 'invalid'
  ans=''
  for i in word:
    if i in "AEIOUaeiou":ans+=i*(num+1)
    else: ans+=i
  return ans

