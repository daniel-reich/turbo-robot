"""


A standard-sized golf course has 18 holes. Each hole is given a _par_ , which
is the expected number of strokes (hits) that a good player would use to
complete a hole. Golf also uses different terms for a player being over/under
par for a particular hole:

  * "eagle" = 2 under par (-2)
  * "birdie" = 1 under par (-1)
  * "bogey" = 1 over par (+1)
  * "double-bogey" = 2 over par (+2)

Example scores:

  * "birdie" on a par 3 hole = 2
  * "eagle" on a par 5 hole = 3
  * "par" on a par 3 hole = 3
  * "bogey" on a par 4 hole = 5

Given a list of pars for an 18-hole golf course, and another list containing
the player result for each hole, return the **total score** for the round of
golf.

### Example

    course = [4, 4, 5, 3, 4, 4, 3, 5, 5, 3, 5, 4, 4, 4, 4, 3, 4, 4]
    
    result = ["eagle", "bogey", "par", "bogey", "double-bogey", "birdie", "bogey", "par", "birdie", "par", "par", "par", "par", "par", "bogey", "eagle", "bogey", "par"]
    
    score = 2+5+5+4+6+3+4+5+4+3+5+4+4+4+5+1+5+4 = 73

### Notes

For this challenge, there will be no _holes-in-one_ , _albatrosses_ (-3), or
anything worse than a double-bogey.

"""

scoring = {'eagle':-2,'birdie':-1
,'par':0,
'bogey':1,
'double-bogey':2,}
​
def golf_score(course, result):
    score = 0
    for cours,reslt in zip(course,result):
        if reslt in scoring.keys():
            score += cours + scoring[reslt]
    return score

