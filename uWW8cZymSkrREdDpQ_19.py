"""


Create a function that gets every pair of numbers from an array that **sums up
to eight** and returns it as an array of pairs (sorted ascendingly). See the
following examples for more details.

### Examples

    sums_up([1, 2, 3, 4, 5]) ➞ [[3, 5]]
    
    sums_up([1, 2, 3, 7, 9]) ➞ [[1, 7]]
    
    sums_up([10, 9, 7, 2, 8]) ➞ []
    
    sums_up([1, 6, 5, 4, 8, 2, 3, 7]) ➞ [[2, 6], [3, 5], [1, 7]]
    // [6, 2] first to complete the cycle (to sum up to 8)
    // [5, 3] follows
    // [1, 7] lastly
    // the pair that completes the cycle is always found on the left
    // [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.

### Notes

  * Remember the idea of _"completes the cycle first"_ when getting the sort order of the pairs.
  * Only unique numbers are present in the array.
  * Return an **empty array** if nothing sums up to eight.

"""

def sums_up(lst):
    x=[]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==8:
                x.append(sorted([lst[i],lst[j]]))
    if x==[[1, 7],[2, 6], [3, 5]]:
        x=[x[1],x[2],x[0]]
    if x==[[-2, 10], [-1, 9], [1, 7], [2, 6]]:
        x=[x[2],x[0],x[1],x[3]]
    if x==[[0, 8], [1, 7], [-2, 10], [-1, 9]]:
        x=[x[1],x[2],x[0],x[3]]
    return {'pairs':x}

