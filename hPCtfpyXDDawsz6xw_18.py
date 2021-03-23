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
  lst = txt.split()
  if lst[0].endswith("e"):
    verb = lst[0] + "d"
  elif lst[0].endswith("ed"):
    verb = lst[0]
  else:
    verb = lst[0] + "ed"
  return ''.join(verb + " " + lst[1])

