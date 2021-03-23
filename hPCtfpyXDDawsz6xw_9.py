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
  if str(txt.split()[0])[-1] in ['a', 'e', 'i', 'o', 'u']:
    return str(txt.split()[0]) + "d " + str(txt.split()[1])
  elif str(txt.split()[0])[-2:] == "ed":
    return txt  
  else:
    return str(txt.split()[0]) + "ed " + str(txt.split()[1])

