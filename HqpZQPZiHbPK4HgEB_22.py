"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def maxmin(n):
  lst = list(map(int, str(n)))
  lst1 = lst[:]
​
  for i, x in enumerate(lst):
    min_index = min(lst[i:])
    most_minimum = min(filter(None, lst))
​
    if not i and x == most_minimum:
      continue
      
    if not i and x != most_minimum:
      min_index= -(lst[::-1].index((min(filter(None, lst)))) + 1)
      lst[0], lst[min_index] = lst[min_index], lst[0]
      break
​
    if x !=  min_index and i:
      min_index = -(lst[::-1].index(min_index) + 1)
      lst[i], lst[min_index] = lst[min_index], lst[i]
      break
  
  final_min = int(''.join(map(str, lst)))
​
  for i, x in enumerate(lst1):
    max_index = max(lst[i:])
    if sorted(lst1, reverse=True) == lst1:
      return (n, final_min)
    
    if x != max_index:
      max_index = -(lst1[::-1].index(max_index) + 1)
      lst1[i], lst1[max_index] = lst1[max_index],lst1[i]
      final_max = int(''.join(map(str, lst1)))
      return (final_max, final_min)

