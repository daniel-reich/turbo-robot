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
  def adds_to_8(n, lst):
    if 8-n in lst and n*2 != 8:
      return sorted([n, 8-n])
    else:
      return False
  def settify(lst):
    sett = []
    for item in lst:
      if item not in sett:
        sett.append(item)
    return sett
  def position(pair, lst):
    positions = []
    for n in range(len(lst)):
      num = lst[n]
      if num in pair:
        positions.append(n)
    return max(positions)
  
  all_pairs = []
  
  for n in lst:
    tst = adds_to_8(n, lst)
    if tst != False:
      all_pairs.append(tst)
# print(all_pairs)
  all_pairs = settify(all_pairs)
  
  positions = {}
  
  for pair in all_pairs:
    positions[position(pair, lst)] = pair
  
  all_pairs = [positions[position] for position in sorted(list(positions.keys()))]
# print(sorted(list(positions.keys())), positions)
  return {'pairs': all_pairs}

