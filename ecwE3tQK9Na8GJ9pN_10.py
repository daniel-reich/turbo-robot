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
    k=0
    t=100
    a=[]
    for i in range(0,n):
        if i%2==0:
            a.append(5+k)
            k+=1
        else:
            a.append(t)
            t=t*2
    return a[n-1]

