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

def football(score):
    if score == 0:
        return 1
    if score == 1:
        return 0
    ctr = 0
    temp = []
    for a in range(score//8+1):
        for b in range(score//7+1):
            for c in range(score//6+1):
                for d in range(score//3+1):
                    for e in range(score//2+1):
                        if a*8+b*7+c*6+d*3+e*2 == score:
                            ctr += 1
                            temp.append([a,b,c,d,e])
                    
    return ctr

