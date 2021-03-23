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
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    total = 0
    #print(total)
    for dice in throw:
        #print(dice)
        if dice == 1:
            a += 1
            #print(a)
        elif dice == 2:
            b += 1
            #print(b)
        elif dice == 3:
            c += 1
            #print(c)
        elif dice == 4:
            d += 1
            #print(d)
        elif dice == 5:
            e += 1
            #print(e)
        else:
            f += 1
            #print(f)
    if a == 3:
        total += 1000
    elif a < 3:
        total += a * 100
    if b == 3:
        total += 200
    if c == 3:
        total += 300
    if d == 3:
        total += 400
    if e == 3:
        total += 500
    elif e < 3:
        total += e * 50
    if f == 3:
        total += 600
    return total

