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
    a = txt.split()
    if a[0][-2:] == "ed":
        return " ".join(a)
    return a[0] + "d" + " " + a[-1] if a[0][-1] == "e" else a[0] + "ed" + " " + a[-1]

