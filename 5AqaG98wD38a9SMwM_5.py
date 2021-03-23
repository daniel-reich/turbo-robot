"""


The _mean_ of a group of numbers is calculated by summing all numbers, and
dividing this sum by the total count of numbers in the group. Given a sorted
list of numbers, return the mean (rounded to one decimal place).

### Examples

    mean([1, 6, 6, 7, 8, 8, 9, 10, 10]) ➞ 7.2
    
    mean([1, 3, 8, 9, 9, 10]) ➞ 6.7
    
    mean([2, 3, 3, 6, 6, 8, 9, 10]) ➞ 5.9

### Notes

N/A

"""

def mean(nums):
    
  Counter = 0
  Items = len(nums) - 1
  Length = len(nums)
  
  Sum = 0
  
  while (Counter < Length):
    Sum += nums[Counter]
    Counter += 1
    
  Mean = Sum/Length
  
  Answer = round(Mean,1)
  
  return Answer

