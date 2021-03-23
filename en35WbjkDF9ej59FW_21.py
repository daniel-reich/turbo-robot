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

def ends_add_to_10(nums):
  if len(nums) > 0:
    x = [abs(i) for i in nums]
    su = sum([1 for i in x if int(str(i)[0]) + int(str(i)[-1]) == 10 ])
    return su
  else:
    return False

