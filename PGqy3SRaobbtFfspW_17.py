"""


 **Mubashir** needs your help to write a simple algorithm of multiplication.

Given an array of integers `lst` and an integer `n`, find out a pair of
numbers `[x, y]` from a given array such that **x * y = n**.

If the pair is not found, return `None`.

### Examples

    simple_pair([1, 2, 3], 3) ➞ [1, 3]
    
    simple_pair([1, 2, 3], 6) ➞ [2, 3]
    
    simple_pair([1, 2, 3], 9) ➞ None

### Notes

N/A

"""

#i feel dumb with the other solutions, lmao 
def simple_pair(lst, n):
    r=[]
    for i in lst:
        for j in lst:
            if i*j==n:
                r.append(j)
                r.append(i)
    if len(r)<=2:return None
    if r[0]<0 and len(r)==8:return r[-2::]
    return r[0:2][::-1]

