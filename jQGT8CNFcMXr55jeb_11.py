"""


Lists can be mixed with various types. Your task for this challenge is to sum
all the number elements in the given list. Create a function that takes a list
and returns the sum of all numbers in the list.

### Examples

    numbers_sum([1, 2, "13", "4", "645"]) ➞ 3
    
    numbers_sum([True, False, "123", "75"]) ➞ 0
    
    numbers_sum([1, 2, 3, 4, 5, True]) ➞ 15

### Notes

Check the **Resources** tab for help.

"""

def numbers_sum(lst):
  total = 0
  for x in lst:
    if isinstance(x, int) and not isinstance(x, bool):
      total = total + x
  return total

