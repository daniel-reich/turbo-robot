"""


Create a function which converts an **ordered** number list into a list of
ranges (represented as strings). Note how some lists have some numbers
missing.

### Examples

    numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]
    
    numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]
    
    numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]
    
    numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

### Notes

  * If there are no numbers consecutive to a number in the list, represent it as only the _string_ version of that number (see example #4).
  * Return an empty list if the given list is empty.

"""

def numbers_to_ranges(lst):
    o=[]
    p=[]
    if len (lst)==1:
        return list(str(lst[0]))
    if len (lst)==0:
        return []
    if sorted(lst) == list(range(min(lst), max(lst)+1)):
        u=("{}-{}".format(lst[0],lst[-1]))
        p.append(u)
        return p
        
    for i in range(0,len(lst)-1):
        o.append(lst[i])
        if lst[i]!=lst[i+1]-1:
            break
    r=o,lst[len(o):]
    if len(o)==1:
        u=str(lst[0])
        l=("{}-{}".format(r[1][0],r[1][-1]))
        p.append(u)
        p.append(l)
        return p
    else:
        
        u=("{}-{}".format(r[0][0],r[0][-1]))
        l=("{}-{}".format(r[1][0],r[1][-1]))
        p.append(u)
        p.append(l)
        return p

