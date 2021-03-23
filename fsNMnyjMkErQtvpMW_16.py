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
    t_v = []
    d = {'4':1,'6':1,'8':2,'0':1,'9':1}
    lst = lst = [str(a) for a in lst]
    for a in lst:
        ls = 0
        for b in a:
            if b in d:
                ls+=d[b]
            else:
                ls+=0
        t_v.append((a,ls))
    a = lambda x:x[1]
    return [int(a[0]) for a in sorted(t_v,key=a,reverse = False)]

