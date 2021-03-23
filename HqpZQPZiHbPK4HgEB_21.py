"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def splitit(v):    
    l = []
    while(v > 0):
        l.append(v % 10)
        v //= 10
    l = l[::-1]
    return l
​
def unSplitit(v):
    n = 0
    for a in v:
        n *= 10
        n += a
    return n
​
def findMax(lst):
    ls = lst[:]
    print(ls)
    for i in range(len(ls)):
        mx = i
        for j in range(len(lst) - 1, i, -1):
            if(ls[j] > ls[mx]):
                mx = j
        if(mx != i):
            tmp = ls[i]
            ls[i] = ls[mx]
            ls[mx] = tmp
            return unSplitit(ls)
    return unSplitit(ls)
​
def findMin(lst):
    ls = lst[:]
    print(ls)
    for i in range(len(ls)):
        mn = i
        for j in range(len(lst) - 1, i, -1):
            if((i == 0) and (lst[j] == 0)):
                continue
            if(ls[j] < ls[mn]):
                mn = j
        if(mn != i):
            tmp = ls[i]
            ls[i] = ls[mn]
            ls[mn] = tmp
            return unSplitit(ls)
    return unSplitit(ls)
​
def maxmin(n):
    lst = splitit(n)
​
    max = findMax(lst)
    min = findMin(lst)
    return (max, min)

