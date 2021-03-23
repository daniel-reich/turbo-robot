"""


Create a function that replaces all the vowels in a string with a specified
character.

### Examples

    replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
    
    replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
    
    replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"

### Notes

All characters will be in lower case.

"""

def replace_vowels(txt, ch):
  l=['a','e','i','o','u']
  x=txt
  for i in txt:
    if i in l:
      x=x.replace(i,ch)
  return x

