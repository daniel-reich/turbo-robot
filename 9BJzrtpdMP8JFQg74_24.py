"""


Create a function that given a list, it returns the index where if split in
two-subarrays (last element of the first array has index of (foundIndex-1)),
the sum of them are equal.

### Examples

    twins([10, 20, 30, 5, 40, 50, 40, 15]) ➞ 5
    # foundIndex 5 : [10+20+30+5+40]=[50+40+15]
    
    twins([1, 2, 3, 4, 5, 5]) ➞ 4
    # [1, 2, 3, 4] [5, 5]
    
    twins([3, 3]) ➞ 1

### Notes

Return only the foundIndex, not the divided list.

"""

def twins(lst):
  sum1 = sum2 = 0
  for x in range(len(lst)):
    for j in range(x+1):
      sum1+=lst[j]
    for i in range(x+1,len(lst)):
      sum2+=lst[i]
    if(sum1 == sum2):
      return x+1
    else:
      sum1 = sum2 = 0

