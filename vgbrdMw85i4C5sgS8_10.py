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
​
    return [drink for drink in drinks if drink != "fanta" and drink != "cola"]
​
    # Alternative way
    # no_sugar_list = []
    # for drink in drinks:
    #     if drink != "fanta" and drink != "cola":
    #         no_sugar_list.append(drink)
    # return no_sugar_list
​
print(skip_the_sugar(["lemonade", "beer", "water"]))

