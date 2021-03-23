"""


The _mode_ of a group of numbers is the value (or values) that occur most
often (values have to occur more than once). Given a sorted list of numbers,
return a list of all modes in ascending order.

### Examples

    mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6] 
    
    mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]
    
    mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6] 

### Notes

In this challenge, all group of numbers will have at least one mode.

"""

def mode(nums):
  dic, max, res = {}, 0, []
  for num in nums:
    k = str(num)
    if k in dic: dic[k] += 1
    else: dic[k] = 1
  for v in dic.values():
    if v > max: max = v
  for k, v in dic.items():
    if v == max: res.append(int(k))
  return sorted(res)

