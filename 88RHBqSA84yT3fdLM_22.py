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

def inator_inator(inv):
  lst = list(inv)
  if lst[len(lst)-1] in 'aeiouAEIOU':
    lst.append("-inator {}000".format(len(lst)))
  else:
    lst.append("inator {}000".format(len(lst)))
  return "".join(lst)

