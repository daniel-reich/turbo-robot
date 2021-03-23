"""


Try to imagine a world in which you might have to stay home for 14 days at any
given time. Do you have enough TP to make it through?

Although the number of squares per roll of TP varies significantly, we'll
assume each roll has 500 sheets, and the average person uses 57 sheets per
day.

Create a function that will receive a dictionary with two key/values:

  * `"people"` ⁠— Number of people in the household.
  * `"tp"` ⁠— Number of rolls.

Return a statement telling the user if they need to buy more TP!

### Examples

    tp_checker({ "people": 4, "tp": 1 }) ➞ "Your TP will only last 2 days, buy more!"
    
    tp_checker({ "people": 3, "tp": 20 }) ➞ "Your TP will last 58 days, no need to panic!"
    
    tp_checker({ "people": 4, "tp": 12 }) ➞ "Your TP will last 26 days, no need to panic!"

### Notes

Stay safe, and happy coding!

"""

import math
def tp_checker(home):
  need = home["people"] * 14 * 57
  have = home["tp"] * 500
  days = math.floor(have/(need/14))
  if have >= need:
    return "Your TP will last " + str(days) +" days, no need to panic!"
  else:
    return "Your TP will only last " + str(days) +" days, buy more!"

