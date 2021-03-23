"""


This challenge will help you interpret mathematical relationships both
algebraically and geometrically.

![Matchstick Houses, Steps 1, 2 and 3](https://edabit-
challenges.s3.amazonaws.com/matchstick_houses.png)

Create a function that takes a number (step) as an argument and returns the
number of matchsticks in that step. See step 1, 2 and 3 in the image above.

### Examples

    match_houses(1) ➞ 6
    
    match_houses(4) ➞ 21
    
    match_houses(87) ➞ 436

### Notes

  * Step 0 returns `0` matchsticks.
  * The input (step) will always be a non-negative integer.
  * Think of the input (step) as the total number of houses that have been connected together.

"""

def match_houses(step):
  if step == 0:
    return 0
  else:
    return 6 * step - (step - 1)

