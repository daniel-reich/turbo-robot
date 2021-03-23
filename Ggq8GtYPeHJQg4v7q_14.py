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
  new_txt=""
  search=['a','e','i','o','u']
  for i in range(len(txt)):
    if txt[i] in search:
      new_txt+=ch
    else:
      new_txt+=txt[i]
  return new_txt

