"""


Scoring plays in American football count as either 2, 3, 6, 7, or 8 points.
Write a function that has as it's argument a football score and returns the
number of possible ways that score can be achieved. Order is not important.

### Examples

    football(4) ➞ 1
    # 2+2
    
    football(6) ➞ 3
    # 2+2+2 or 3+3 or 6
    
    football(7) ➞ 2
    # 2+2+3 or 7
    
    football(9) ➞ 4
    # 2+2+2+3 or 3+3+3 or 3+6 or 7+2

### Notes

N/A

"""

def combines(s, m, n):
    if n < 0 or m <= 0:
        return 0
    if n == 0:
        return 1
    if m == 1:
        if n%s[0] == 0:
            return 1
        else:
            return 0
    
    total = combines(s, m-1, n) + combines(s,m,n-s[m-1])
    return total
​
def football(n):
    scores = [2,3,6,7,8]
    if n == 0:
        return 1
    if n ==1:
        return 0
​
    total = combines(scores, len(scores),n)
    return total

