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
  return sum(int(str(abs(n))[0]) + abs(n) % 10 == 10 for n in nums)
