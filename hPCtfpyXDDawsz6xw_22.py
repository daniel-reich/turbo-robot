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
    txt=txt.split()
    if  txt[0].endswith("ed"): 
        txt[0]=txt[0]+" "
        return "".join(txt)
    elif txt[0].endswith("e"):
        txt[0]=txt[0]+"d"+" "
        return "".join(txt)
    else:
        txt[0]=txt[0]+"ed"+" "
        return "".join(txt)
