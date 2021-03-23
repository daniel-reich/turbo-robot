"""


Write a function that returns all sets of three elements that sum to 0.

### Examples

    three_sum([0, 1, -1, -1, 2]) ➞ [[0, 1, -1], [-1, -1, 2]]
    
    three_sum([0, 0, 0, 5, -5]) ➞ [[0, 0, 0], [0, 5, -5]]
    
    three_sum([1, 2, 3]) ➞ []
    
    three_sum([1]) ➞ []

### Notes

  * The original list **may contain duplicate numbers**.
  * Each three-element sublist in your output should be **distinct**.
  * Sublists should be ordered by the first element of the sublist.
  * Sublists themselves should be ordered the same as the original list.
  * Return an empty list if no three elements sum to zero.
  * Return an empty list if there are fewer than three elements.

"""

def three_sum(lst):
  if len(lst)<3: return []
  l=[]
  for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
      for k in range(j+1,len(lst)):
        if lst[i]+lst[j]+lst[k]==0 and [lst[i],lst[j],lst[k]] not in l: l.append([lst[i],lst[j],lst[k]])
  return l

