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

from collections import OrderedDict  
def dice_score(throw):
​
    def group_list(lst): 
        res =  [(el, lst.count(el)) for el in lst] 
        return list(OrderedDict(res).items()) 
​
    group = group_list(throw)
    total_score = 0
    for i in group:
        value = i[0]
        count = i[1]
        points = 0
        total_points = 0
​
        if value == 1 and count == 3:
            points = 1000
        elif value == 2 and count == 3:
            points = 200
        elif value == 3 and count == 3:
            points = 300
        elif value == 4 and count == 3:
            points = 400
        elif value == 5 and count == 3:
            points = 500
        elif value == 6 and count == 3:
            points = 600
        elif value == 1:
            points = 100
        elif value == 5:
            points = 50
        else:
            points = 0
    
​
        print('value:', value, 'count:', count, 'point value:', points)
​
        total_score += points
    
    return(total_score)

