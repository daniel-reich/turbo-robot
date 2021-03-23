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

def sums_up(nums):
  result = [
    (sorted((number, n)), index + i)
    for index, number in enumerate(nums)
    for i, n in enumerate(nums[index + 1:])
    if number + n == 8
  ]
  result.sort(key=lambda r: r[1])
  return {'pairs': [r[0] for r in result]}

