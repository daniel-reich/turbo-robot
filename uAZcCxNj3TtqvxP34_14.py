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

from collections import Counter
def mode(nums):
    z=[]
    m=[]
    count=0
    d=Counter(nums)
    for key,values in d.items():
        z.append(values)
      
    for i,t in d.items():
        if t==max(z):
            count=count+1
            m.append(i)
       
   
    if count!=1:
        return sorted(m)
    else:
        return m

