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

#
# [3, 6, 8, 11, 15, 19, 22], 3, 35), ["8-8-19"]
#
def darts_solver (sections, darts, target) :  
    solutions = set() # solution set
    add_dart(sections, darts, [], target, solutions)
    solutions.remove(None)
    return list(solutions)
            
# spin through the possible throws and determine if a solution is found
def add_dart(sections, darts, throws, target, solutions) :
    
    count = len(throws)
    
    # if this is too many darts, we have failed.
    if count > darts :
        return "None"
    
    #increment the throw count
    count += 1
    
    for t in sections :
        throws.append(t)
​
        # we found a solution
        if (sum(throws) == target and count == darts) :
            solutions.add(throw_solution(throws))
​
            # if we still have more throws call add_dart again
        elif count < darts :
            pot_sol = add_dart(sections, darts, throws, target, solutions) 
            if (pot_sol != 'None') :
                solutions.add(pot_sol)
        
        # if we made it this far, we haven't found a solution
        throws.pop()
    
   
def throw_solution(throws) :
    """
    Input:
        list of dart throws
        
    Return:
        Formatted string of throws separated by dashes
            ex: 3-8-25
    """
    throws.sort()
    sol = str(throws[0])
    for s in throws[1:-1] :
        sol += "-" + str(s)
    
    sol +=  "-" + str(throws[-1])
    
    return sol

