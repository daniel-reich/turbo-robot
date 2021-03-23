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

def darts_solver(sections, darts, target):
    ixs = [0] * darts
    i_ix = len(ixs)-1
    res = []
    while 1:
        curr_subset = [sections[i] for i in ixs]
        curr_sum = sum(curr_subset)
        if curr_sum >= target or ixs[i_ix] == len(sections)-1:
            if curr_sum == target:
                res.append(curr_subset)
            i = ixs[i_ix]
            i_ix -= 1
            while i_ix >= 0:
                if ixs[i_ix] < i:
                    ixs[i_ix] += 1
                    for j in range(i_ix+1, len(ixs)):
                        ixs[j] = ixs[i_ix]
                    i_ix = len(ixs) - 1
                    break
                i_ix -= 1
            if i_ix < 0:
                break
        else:
            # increment
            ixs[i_ix] += 1
    return ['-'.join([str(y) for y in x]) for x in sorted(res)]

