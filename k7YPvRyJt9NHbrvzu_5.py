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

points = [2, 3, 6, 7, 8]
lookup = {}
def football(score, n=4):
    if score == 0: return 1
    if score < 0 or n < 0: return 0
    key = (n, score)
    if key in lookup:
        res = lookup[key]
    else:
        res = football(score-points[n], n) + football(score, n-1)
        lookup[key] = res
    return res

