"""


Create a function that takes a single word string and does the following:

  1. Concatenates `inator` to the end if the word ends with a consonant, otherwise, concatenate `-inator` instead.

  2. Adds the word length of the original word to the end, supplied with "000".

The examples should make this clear.

### Examples

    inator_inator("Shrink") ➞ "Shrinkinator 6000"
    
    inator_inator("Doom") ➞ "Doominator 4000"
    
    inator_inator("EvilClone") ➞ "EvilClone-inator 9000"

### Notes

For the purposes of this challenge, vowels will be **a, e, i, o** and **u**
only.

"""

def inatorInator(inv):
​
  print(inv)
  print(inv[-1])
  print(inv[-1].lower())
  
  if inv[-1].lower() == 'a' or inv[-1].lower() == 'e' or inv[-1].lower() == 'i' or inv[-1].lower() == 'o' or inv[-1].lower() == 'u':
    new_inv = inv + '-inator '
    
  else:
    new_inv = inv + 'inator '
    
  return new_inv + str(len(inv)) + '000'

