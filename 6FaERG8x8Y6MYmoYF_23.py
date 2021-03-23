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
  c_o = 0
  c_t = 0
  c_th = 0
  c_f = 0
  c_fi = 0
  c_s = 0
  for num in throw:
    if num == 1:
      c_o+=1
    elif num == 2:
      c_t+=1
    elif num == 3:
      c_th+=1
    elif num == 4:
      c_f+=1
    elif num == 5:
      c_fi+=1
    else:
      c_s+=1
  score = 0
  
  if c_o == 3:
    score = score + 1000
  elif c_o == 1:
    score = score + 100
  
  if c_t == 3:
    score = score + 200
    
  if c_th == 3:
    score = score + 300
  
  if c_f == 3:
    score = score + 400
  
  if c_fi == 3:
    score = score + 500
  elif c_fi == 1:
    score = score + 50
  
  if c_s == 3:
    score = score + 600
  return score

