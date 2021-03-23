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

def verbify(n):
     return n.split( )[0]+'d'+' '+ n.split( )[1] if n.split( )[0].endswith('e') else n.split( )[0]+' '+ n.split( )[1] if n.split( )[0].endswith('ed') else n.split( )[0]+'ed'+' '+ n.split( )[1]

