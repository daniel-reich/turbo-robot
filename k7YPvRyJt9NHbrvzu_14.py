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

ps=(2,3,6,7,8)
def football(n):
    ret=set()
    for i in range(0,n//ps[0]+1):
        for j in range(0,n//ps[1]+1):
            for k in range(0,n//ps[2]+1):
                for l in range(0,n//ps[3]+1):
                    for m in range(0,n//ps[4]+1):
                        if n==i*ps[0]+j*ps[1]+k*ps[2]+l*ps[3]+m*ps[4]:
                            ret=ret|{(i,j,k,l,m)}
    return len(ret)

