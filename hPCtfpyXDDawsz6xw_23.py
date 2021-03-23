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
  converted=txt.split()
  ans=""
  if converted[0][-2:]=="ed":
    return txt
  elif converted[0][-1]=="e":
    ans+=converted[0]+"d "+converted[1]
    return ans
  else:
    ans+=converted[0]+"ed "+converted[1]
    return ans

