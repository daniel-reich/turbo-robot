"""


Write a function that takes a list of drinks and returns a list of only drinks
with **no sugar** in them. Drinks that contain sugar (in this challenge) are:

  * Cola
  * Fanta

### Examples

    skip_the_sugar(["fanta", "cola", "water"]) ➞ ["water"]
    
    skip_the_sugar(["fanta", "cola"]) ➞ []
    
    skip_the_sugar(["lemonade", "beer", "water"]) ➞ ["lemonade", "beer", "water"]

### Notes

  * The function returns an array of strings.
  * All drink names are in lowercase.

"""

def skip_the_sugar(drinks):
  return [i for i in drinks if i != "cola" and i != "fanta"]

