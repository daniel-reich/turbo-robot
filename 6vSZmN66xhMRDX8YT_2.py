"""


Create a function that takes a list of **numbers or strings** and returns a
list with the items from the original list stored into sublists. Items of the
same value should be in the same sublist.

### Examples

    advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
    
    advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
    
    advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

### Notes

The sublists should be returned in the order of each element's first
appearance in the given list.

"""

def advanced_sort(lst):
  r=[]
  while(len(lst)):
    p=lst[0]
    r+=[[p]*lst.count(p)]
    for i in range(lst.count(p)):
      lst.remove(p)
  return r
