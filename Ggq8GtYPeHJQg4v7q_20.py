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
  exit_txt = ''
  for char in txt:
    if char in ['a', 'e', 'i', 'o', 'u']:
      exit_txt += ch
    else:
      exit_txt += char
    
  return exit_txt

