"""


Greed is a dice game played with five six-sided dices. Your mission is to
score a throw according to these rules:

     Three 1's => 1000 points
     Three 6's =>  600 points
     Three 5's =>  500 points
     Three 4's =>  400 points
     Three 3's =>  300 points
     Three 2's =>  200 points
     One   1   =>  100 points
     One   5   =>   50 point

See the below examples for a better understanding:

     Throw       Score
     ---------   ------------------
     5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
     1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
     2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

Create a function that takes a list of five six-sided **throw values** and
returns the final calculated **dice score**.

### Examples

    dice_score([2, 3, 4, 6, 2]) ➞ 0
    
    dice_score([4, 4, 4, 3, 3]) ➞ 400
    
    dice_score([2, 4, 4, 5, 4]) ➞ 450

### Notes

A single dice can only be counted once in each roll. For example, a given "5"
can only be counted as a part of the triplet (contributing to the 500 points)
or as a single 50 points, but not both in the same roll.

"""

def dice_score(throw):
  sum = 0
  x = throw.count(1)
  if x >= 3:
    sum = sum + 1000 +(x-3)*100
  else:
    sum = sum + x * 100
  y = throw.count(2)
  if y >= 3:
    sum = sum + 200 
  z = throw.count(3)
  if z >= 3:
    sum = sum + 300
  m = throw.count(4)
  if m >= 3:
    sum = sum + 400
  n = throw.count(5)
  if n >= 3:
    sum = sum + 500 +(n-3)*50
  else:
    sum = sum + n *50
  o = throw.count(6)
  if o >= 3:
    sum = sum + 600
   
  return sum

