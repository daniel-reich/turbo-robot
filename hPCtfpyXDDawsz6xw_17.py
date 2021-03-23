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
  if txt.split()[0].endswith("ed"):
    return txt
  elif txt.split()[0].endswith("e"):
    return txt.split()[0]+"d" +" " + txt.split()[1]
  else:
    return txt.split()[0]+"ed" +" " + txt.split()[1]

