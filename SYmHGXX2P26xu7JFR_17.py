"""


Given three groups of numbers, return a list containing all numbers that
appear in more than one group (in ascending order).

### Examples

    number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) ➞ []
    
    number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) ➞ [1, 3]
    
    number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]) ➞ [2, 4, 9]
    
    number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]) ➞ [5, 8]

### Notes

N/A

"""

def number_groups(group1, group2, group3):
    z=[]
    h=[]
    a=set(group1)
    b=set(group2)
    c=set(group3)
    p=a.intersection(b)
    
    k=a.intersection(c)
    l=b.intersection(c)
    print(p,k,l)
    if p==set() and k==set():
        return  sorted(list(l))
    elif p==set() and l==set():
        return sorted(list(k))
    elif k==set() and l==set():
        return sorted(list(p))
​
   
    elif k==set():
        d=list(l)
        
        g=list(p)
        for u in d:
            g.append(u)
        g=list(set(g))
       
        return  sorted(g)
    elif p==set():
        d=list(l)
        
        g=list(k)
        for r in d:
            g.append(r)
        g=list(set(g))
     
        return sorted(g)
    elif l==set():
        d=list(p)
        
        g=list(k)
        for e in d:
            g.append(e)
        g=list(set(g))
        return sorted(g)
    elif ((p!=set() and k!=set()) and (l!=set())):
        x=list(p)
        y=list(k)
        z=list(l)
        for i in y:
            x.append(i)
        for j in z:
            x.append(j)
        x=list(set(x))
        return sorted(x)
    else:
        return []

