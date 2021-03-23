"""


Find the length of the longest sub-sequence of two distinct numbers whose
difference is `1`. A sub-sequence can be made by deleting any numbers in
between.

### Examples

    almost_uniform([1, 3, 2, 2, 5, 2, 3, 7]) ➞ 5
    # [3, 2, 2, 2, 3]
    
    almost_uniform([1, 2, 3, 4]) ➞ 2
    # [1, 2] or [2, 3] or [3, 4]
    
    almost_uniform([1, 1, 1, 1]) ➞ 0
    # There is no sub-sequence of two distinct numbers.

### Notes

N/A

"""

def almost_uniform(nums):
  
  Ordered = set(nums)
  Ordered = sorted(list(Ordered))
  
  Answer = 0
  
  First = 0
  Second = 1
  Length = len(Ordered)
  
  while (Second < Length):
    
    Value_A = Ordered[First]
    Value_B = Ordered[Second]
    Difference = Value_B - Value_A
    
    Score_A = nums.count(Value_A)
    Score_B = nums.count(Value_B)
    Total = Score_A + Score_B
    
    if (Difference != 1):
      First += 1
      Second += 1
    elif (Total <= Answer):
      First += 1
      Second += 1
    else:
      Answer = Total
      First += 1
      Second += 1
  
  return Answer

