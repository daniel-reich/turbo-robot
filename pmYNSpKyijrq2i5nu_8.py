"""


You're given a dartboard divided into sections, each section has a **unique**
score. That means there won't be two sections with the same score.

![alt text](https://s3.amazonaws.com/edabit-images/dartboard.png)

Throwing a certain amount of valid darts, find how many solutions there are to
reach the target score. Your function will be passed three parameters...

  *  **Sections** : A list of values for the sections (e.g. `[3, 6, 8, 11, 15, 19, 22]`, the list is already sorted).

  *  **Darts** : The amount of darts to throw.

  *  **Target** : The target score.

Return an empty list if no solution is found, otherwise a list of non-
duplicate strings for each solution (e.g. `["3-11-18", "7-7-18", "7-11-14"]`).

### Examples

If there are duplicate values, keep only the one sorted from smallest to
biggest.

    "8-19-8"
    
    "8-8-19" <-- This is the one you would keep.
    
    "19-8-8"

Multiple solutions should be sorted before returning them.

    ["3-11-18", "7-7-18", "7-11-14"] is ok.
    
    ["7-11-14", "7-7-18", "3-11-18"] is not ok.

### Notes

  * Multiple darts **can** land in the same section.
  * A dart **must** land in a valid section (it can't miss).

"""

import itertools
​
def darts_solver(sections, darts, target):
  score_list = list(itertools.product(sections, repeat=darts))
  solution_list = []
  score_set = []
  s_set = []
  
  for score in score_list:
    s = [x for x in score]
    s.sort()
    if s not in s_set:
      s_set.append(s)
      score_set.append(score)
      
  for score in score_set: 
    if sum(score) == target:
      s = [str(x) for x in score]
      score_string = "-".join(s)
      solution_list.append(score_string)
      
  return solution_list
