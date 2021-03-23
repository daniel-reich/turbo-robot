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
    j=txt.split()
    if j[0][-2:]=="ed":
        return txt
    elif j[0][-1]=="e":
        return j[0]+"d"+" "+j[1]
    else:
        return j[0]+"ed"+" "+j[1]

