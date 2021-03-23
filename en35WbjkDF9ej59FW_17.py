"""


Given a list of numbers, of any length, create a function which counts how
many of those numbers pass the following criterea:

  * The **first** and **last** digits of a number must add to **10**.

### Examples

    ends_add_to_10([19, 46, 2098]) ➞ 3
    
    ends_add_to_10([33, 44, -55]) ➞ 1
    
    ends_add_to_10([]) ➞ 0

### Notes

  * All items in the list will be numbers.
  * Ignore negative signs (see example #2).
  * If given an empty list, return `0`.

"""

import math
def ends_add_to_10(nums):
  for i in range(0,len(nums)):
    if nums[i] < 0:
      nums[i] *= -1
  tally = 0
  brr = map(str,nums)
  for x in brr:
    if int(list(x)[0]) + int(list(x)[-1]) == 10:
      tally += 1
  return tally

