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
    t = txt.split()
    if t[0][-1] == 'e' or t[0][-1] == 'd':
        if t[0][-1] == 'e':
            t[0] += 'd'
        elif t[0][-2] != 'e':
            t[0] += 'ed'
    else:
        t[0] += 'ed'
    return ' '.join(t)

