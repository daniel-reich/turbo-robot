"""


Given a positive integer `n`, implement a function that finds the **smallest**
number that is evenly divisible by the integers `1` through `n` inclusive.

### Examples

    smallest(1) ➞ 1
    
    smallest(5) ➞ 60
    
    smallest(10) ➞ 2520
    
    smallest(20) ➞ 232792560

### Notes

N/A

"""

def smallest(n):
    def factors(n):
        res=[]
        for i in range(2,n+1):
            while True:            
                if n%i==0:
                    res.append(i)
                    n=n//i
                else:
                    break
        return res
    factlist,prod=[],1
    for i in range(2,n+1):
        f=factlist[:]
        for elem in factors(i):            
            if elem in f:
                f.remove(elem)
            else:
                factlist.append(elem)
                prod*=elem
    return prod

