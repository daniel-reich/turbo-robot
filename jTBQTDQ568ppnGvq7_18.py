"""


Write a function that sorts a list of integers by their digit length in
**descending order** , then settles ties by sorting numbers with the same
digit length in **ascending order**.

### Examples

    digit_sort([77, 23, 5, 7, 101])
    ➞ [101, 23, 77, 5, 7]
    
    digit_sort([1, 5, 9, 2, 789, 563, 444])
    ➞ [444, 563, 789, 1, 2, 5, 9]
    
    digit_sort([53219, 3772, 564, 32, 1])
    ➞ [53219, 3772, 564, 32, 1]

### Notes

N/A

"""

import itertools
​
def digit_sort(lst):
  lst=[str(x) for x in lst]
  lst.sort(key=len,reverse=True)
  res=[]
  for k,g in itertools.groupby(lst,key=len):
    for x in sorted(g):
      res.append(int(x))
  return res

