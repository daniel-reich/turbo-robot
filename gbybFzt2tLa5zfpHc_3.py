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

from itertools import combinations
def three_sum(lst):
    x,a=[],[]
    if len(lst)<3:
        return []
    else:
        comb =combinations(lst, 3)
        for i in comb:
            if sum(list(i))==0:
                x.append(list(i)) 
        dups=set()
        for i,route in enumerate(x):
            if tuple(route) in dups:
                a.append(i)
            else:
                dups.add(tuple(route))
        if len(a)==2:
            return x[:2]
        if len(a)==1:
            x.pop(a[0])
            return x
        if len(a)==3:
            x.pop(a[2])
            x.pop(a[1])
            x.pop(a[0])
            return x
        else:
            return x

