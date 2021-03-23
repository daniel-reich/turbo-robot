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

def do_darts_solver(s, n, t, accD, accS):
  if n == 0 and t == 0:
    accS.add(tuple(accD))
  elif n > 0 and t > 0 and len(s):
    d = s.pop()
    do_darts_solver(list(s), n, t, accD, accS)
    do_darts_solver(list(s), n-1, t-d, accD+[d], accS)
    do_darts_solver(list(s)+[d], n-1, t-d, accD+[d], accS)
  return accS
​
def darts_solver(sections, darts, target):
  darts = do_darts_solver(sorted(sections, reverse=True), darts, target, [], set([]))
  return ['-'.join(str(x) for x in d) for d in sorted(darts)]

