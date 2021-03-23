"""


Create a function that adds a string ending to each member in a list.

### Examples

    add_ending(["clever", "meek", "hurried", "nice"], "ly")
    ➞ ["cleverly", "meekly", "hurriedly", "nicely"]
    
    add_ending(["new", "pander", "scoop"], "er")
    ➞ ["newer", "panderer", "scooper"]
    
    add_ending(["bend", "sharpen", "mean"], "ing")
    ➞ ["bending", "sharpening", "meaning"]

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

newlst = []
def add_ending(lst, ending):
  output = ["{}{}".format(i,ending) for i in lst]
  return output

