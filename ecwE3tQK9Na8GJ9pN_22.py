"""


A number sequence is as follows:

    5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200, ...

Given that `5` is at position **1** , create a function that returns the
number found at position `n` in the sequence.

### Examples

    little_big(4) ➞ 200
    
    little_big(5) ➞ 7
    
    little_big(28) ➞ 819200

### Notes

You can expect to be only given valid inputs.

"""

def little_big(n):
    
    l1 = [i for i in range(5,101)]
    l2 = []
    l3 = []
    a = 50
    b = 0
    
    while b < 20:
        a = a * 2
        l2.append(a)
        b = b + 1
    
    for i,j in zip(l1,l2):
        l3.append(i)
        l3.append(j)
    
    for i in l3:
        if l3.index(i) == n-1:
            return i

