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
  l = txt.split(" ")
  if l[0].endswith("ed"): return txt
  if l[0].endswith("e"):  return "{}d {}".format(l[0],l[1])
  else: return "{}ed {}".format(l[0],l[1])

