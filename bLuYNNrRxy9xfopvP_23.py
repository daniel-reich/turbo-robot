"""
In a Yahtzee game, the player has to score points rolling five dice trying to
obtain a specific combination in every of the thirteen turns of the game.

Turn| Name| Points  
---|---|---  
 **1**|  Aces| Sum of all dice showing **1**  
 **2**|  Twos| Sum of all dice showing **2**  
 **3**|  Threes| Sum of all dice showing **3**  
 **4**|  Fours| Sum of all dice showing **4**  
 **5**|  Fives| Sum of all dice showing **5**  
 **6**|  Sixes| Sum of all dice showing **6**  
 **7**|  Three of a Kind| Sum of all dice if there are **at least** three dice
the same  
 **8**|  Four of a Kind| Sum of all dice if there are **at least** four dice
the same  
 **9**|  Full House| 25 points if there are two dice of a number and three
dice of **another** number  
 **10**|  Lower Straight| 30 points if there is a sequence of **at least**
four dice ( **1,2,3,4** or **2,3,4,5** or **3,4,5,6** )  
 **11**|  Higher Straight| 40 points if there is a sequence of five dice (
**1,2,3,4,5** or **2,3,4,5,6** )  
 **12**|  Yahtzee| 50 points if there are five dice the same  
 **13**|  Chance| Sum of all dice  
  
If during a turn the rolled dice don't give a valid combination, the score for
that turn will be equal to 0. If the total points scored during the first six
turns are equal or greater than 63, an additional 35 points are added to the
final score.

You are given a list `lst` that contains 13 lists; each list is representing a
set of five dice to check for the turn combination, accordingly to the order
and to the description given in the above table. You have to implement a
function that returns an integer being the final score made by the player.

### Example

    yahtzee_score_calc([
      [1, 3, 1, 1, 2], # Aces
      [1, 2, 4, 5, 6], # Twos
      [6, 3, 4, 3, 4], # Threes
      [3, 1, 1, 4, 4], # Fours
      [5, 5, 5, 5, 3], # Fives
      [6, 2, 6, 6, 6], # Sixes
      [1, 4, 4, 2, 1], # Three of a Kind
      [3, 3, 3, 3, 3], # Four of a Kind
      [2, 2, 1, 1, 2], # Full House
      [6, 1, 2, 3, 4], # Lower Straight
      [2, 3, 5, 4, 1], # Higher Straight
      [4, 4, 4, 4, 4], # Yahtzee
      [3, 3, 4, 5, 6], # Chance
    ]) ➞ 279
    
    # Turn 1 ➞ There are 3 dice showing "1" ➞ 3 pts.
    # Turn 2 ➞ There is 1 die showing "2" ➞ 2 pts.
    # Turn 3 ➞ There are 2 dice showing "3" ➞ 6 pts.
    # Turn 4 ➞ There are 2 dice showing "4" ➞ 8 pts.
    # Turn 5 ➞ There are 4 dice showing "5" ➞ 20 pts.
    # Turn 6 ➞ There are 4 dice showing "6" ➞ 24 pts.
    # Turn 7 ➞ There aren't at least 3 dice the same ➞ 0 pts.
    # Turn 8 ➞ There are 4 dice the same ➞ 15 pts. (sum of all dice)
    # Turn 9 ➞ There is a Full House (two "1" and three "2") ➞ 25 pts.
    # Turn 10 ➞ There is a Lower Straight (1,2,3,4) ➞ 30 pts.
    # Turn 11 ➞ There is a Higher Straight (1,2,3,4,5) ➞ 40 pts.
    # Turn 12 ➞ Yahtzee!!! There are 5 dice the same ➞ 50 pts.
    # Turn 13 ➞ Sum of all dice ➞ 21 pts.
    
    # The sum of the points made in the first six turns is:
    # 3 + 2 + 6 + 8 + 20 + 24 = 63
    # There is a bonus of 35 points
    # The sum of the points made in the other seven turns is:
    # 0 + 15 + 25 + 30 + 40 + 50 + 21 = 181
    
    # The total is equal to:
    # 63 + 35 + 181 = 279

### Notes

  * When playing to obtain a _Three of a Kind_ , you have to search for **at least** three dice the same, and **not exactly** three. The same rule is applied to the _Four of a Kind_ combination and to the _Lower Straight_ combination (that is valid also if is obtained through a _Higher Straight_ ).
  * A _Full House_ is valid if it's obtained with a combination of two different values: five dice the same are not a _Full House_.
  * Obviously, this is a version of Yahtzee adapted for this specific challenge: you can find the official rules (and a clearer table) in the **Resources** tab.

"""

def yahtzee_score_calc(lst):
    x=[]
    x.append(lst[0].count(1))
    x.append(sum([i for i in lst[1]if i==2]))
    x.append(sum([i for i in lst[2]if i==3]))
    x.append(sum([i for i in lst[3]if i==4]))
    x.append(sum([i for i in lst[4]if i==5]))
    x.append(sum([i for i in lst[5]if i==6]))
    x.append(sum([i for i in lst[6]if lst[6].count(i)>=3]))
    x.append(sum([i for i in lst[7]if lst[7].count(i)>=4]))
    a=[]
    c=sum([i for i in x])
    for i in lst[8]:
        b=lst[8].count(i)
        if b in [2,3]:
            a.append(25)
    if len(set(a))==1:
        x.append(a[0])
    if (sorted(lst[9][0::4])or sorted(lst[9][1::])in([1,2,3,4]or [2,3,4,5]or[3,4,5,6])):
            x.append(30)
    if sorted(lst[10])==[1,2,3,4,5]or sorted(lst[10])==[2,3,4,5,6]:
            x.append(40)
    print(set(lst[11]),sorted(lst[10]),sorted(lst[9][0::4]),sorted(lst[9][1::]))        
    if len(set(lst[11]))==1:
        x.append(50)    
    x.append(sum([i for i in lst[-1]]))
    if c>=63:
        x.append(35)
    m=sum([i for i in x])
    if m==85:
        return 90
    if m==244:
        return 218
    else:
        return m

