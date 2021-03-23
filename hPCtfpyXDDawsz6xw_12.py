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
  txt1, txt2 = txt.split()[0], txt.split()[1]
  if txt1.endswith('ed'):
    return txt
​
  elif txt1.endswith('e'):
    return '{}d {}'.format(txt1, txt2)
​
  return '{}ed {}'.format(txt1,txt2)

