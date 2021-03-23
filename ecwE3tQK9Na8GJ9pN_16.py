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
    seq = [5, 100]
    c = 0
    d = 5
    e = 100
    while c < 14:
        d = d + 1
        e = e * 2
        seq.append(d)
        seq.append(e)
        c = c + 1
​
    return seq[n-1]

