"""


Create a function that ends the first word of a phrase with `"ed"`,
essentially _verbifying_ a noun.

### Examples

    verbify("cheese burger") ➞ "cheesed burger"
    
    verbify("salt water") ➞ "salted water"
    
    verbify("orange juice") ➞ "oranged juice"
    
    verbify("shredded cheese") ➞ "shredded cheese"

### Notes

  * Change only the **first** word.
  * Note that some words may _already_ end in `"e"` or `"ed"`.
  * All phrases will be in lowercase.

"""

def verbify(txt):
  splitted_text = txt.split()
  if splitted_text[0][-1] == 'e':
    splitted_text[0] = ''.join([splitted_text[0], 'd'])
  elif splitted_text[0][-2:] != 'ed':
    splitted_text[0] = ''.join([splitted_text[0], 'ed'])
  return ' '.join(splitted_text)

