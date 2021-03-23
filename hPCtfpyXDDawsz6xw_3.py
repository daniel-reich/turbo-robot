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
  
  words = txt.split()
  
  if words[0][-1] == 'e':
    words[0] += 'd'
  elif words[0][-2:] == 'ed':
    words[0] = words[0]
  else:
    words[0] += 'ed'
  
  return ' '.join(words)

