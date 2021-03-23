"""


 _What do the numbers 4, 6, 8, 9 and 0 have in common? They all have holes in
them! Notice how the number 8 contains not one, but two holes._

Given a list of numbers, sort the list in accordance to how many holes occur
in the number. It should be sorted in **ascending order**.

### Examples

    holey_sort([44, 4, 444, 4444]) ➞ [4, 44, 444, 4444]
    
    holey_sort([100, 888, 1660, 11]) ➞ [11, 100, 1660, 888]
    
    holey_sort([8, 121, 41, 66]) ➞ [121, 41, 8, 66]

### Notes

  * If two numbers have the same number of holes in them, sort them by the order they first appeared in.
  * Despite the number 0 appearing to have _two holes_ in certain fonts, it will only have **one hole** for the purposes of this challenge.

"""

def holey_sort(lst):
  import operator
  h = ['0','4','6','8','9']
  n = [sum([2 if i=='8' else 1 if i in h else 0 for i in str(x)]) for x in lst]
  z = [x for x in zip(lst,n)]
  l = []
  if set(n)!=len(lst):
    for y in range(max(n)+1):
      for k,v in z:
        if v==y:  l.append(k)
  return l

