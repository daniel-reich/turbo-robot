"""


Create a function that takes in an array of grass heights and a **variable**
sequence of lawn mower cuts and outputs the array of successive grass heights.

If **after a cut** , any single element in the array reaches zero or negative,
return `"Done"` instead of the array of new heights.

A demo:

    cutting_grass([3, 4, 4, 4], 1, 1, 1) ➞ [[2, 3, 3, 3], [1, 2, 2, 2], "Done"]
    
    # 1st cut shaves off 1: [3, 4, 4, 4] ➞ [2, 3, 3, 3]
    # 2nd cut shaves off 1: [2, 3, 3, 3] ➞ [1, 2, 2, 2]
    # 3rd cut shaves off 1: [1, 2, 2, 2]➞ [0, 1, 1, 1], but one element reached zero so we return "Done".

### Examples

    cutting_grass([4, 4, 4, 4], 1, 1, 1, 1)
    ➞ [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], "Done"]
    
    cutting_grass([5, 6, 7, 5], 1, 2, 1)
    ➞ [[4, 5, 6, 4], [2, 3, 4, 2], [1, 2, 3, 1]]
    
    cutting_grass([8, 9, 9, 8, 8], 2, 3, 2, 1)
    ➞ [[6, 7, 7, 6, 6], [3, 4, 4, 3, 3], [1, 2, 2, 1, 1], "Done"]
    
    cutting_grass([1, 0, 1, 1], 1, 1, 1) ➞ ["Done", "Done", "Done"]

### Notes

  * The number of lawn cuts is variable.
  * There will be at least one cut.
  * Return `"Done"` onwards for each additional cut if the grass has already been completely mowed (see fourth example).

"""

def cutting_grass(lst, *cuts):
  def to_cut(lst, cut):
    nl = []
    for item in lst:
      nl.append(item - cut)
    return nl
  
  results = []
  l = lst
  for cut in cuts:
    if l != 'Done':
      c = to_cut(l, cut)
      if 0 in c:
        results.append('Done')
      else:
        results.append(c)
​
      l = results[-1]
    else:
      results.append('Done')
  
  return results

