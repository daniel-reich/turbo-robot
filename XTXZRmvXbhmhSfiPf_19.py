"""


The function is given a list of numbers where each number appears three times
except for one which appears only one time. Find the single number and return
it.

### Examples

    single_number([2, 2, 3, 2]) ➞ 3
    
    single_number([0, 1, 0, 1, 0, 1, 99]) ➞ 99
    
    single_number([-1, 2, -4, 20, -1, 2, -4, -4, 2, -1]) ➞ 20

### Notes

To run under 12 seconds the function needs to be efficient.

"""

def single_number(nums):
  
  Unique = set(nums)
  Seeking = sorted(list(Unique))
  
  Counter = 0
  Length = len(Seeking)
  
  while (Counter < Length):
    Item = Seeking[Counter]
    Events = nums.count(Item)
    
    if (Events == 1):
      return Item
    else:
      Counter += 1
  
  return "No unique items :-)"

