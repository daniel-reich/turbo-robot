"""


Write **two** functions:

  1. One that returns the **maximum product** of three numbers in a list.
  2. One that returns the **minimum product** of three numbers in a list.

### Examples

    max_product([-8, -9, 1, 2, 7]) ➞ 504
    
    max_product([-8, 1, 2, 7, 9]) ➞ 126
    
    min_product([1, -1, 1, 1]) ➞ -1
    
    min_product([-5, -3, -1, 0, 4]) ➞ -15

### Notes

N/A

"""

def max_product(lst):
    import itertools
    comblst=[]
    for comb in itertools.combinations(lst, 3):
        comblst.append(comb)
    #print(comblst)
    anslst = sorted([i[0]*i[1]*i[2] for i in comblst])
    return anslst[-1] 
​
def min_product(lst):
    import itertools
    comblst=[]
    for comb in itertools.combinations(lst, 3):
        comblst.append(comb)
    #print(comblst)
    anslst = sorted([i[0]*i[1]*i[2] for i in comblst])
    return anslst[0]

