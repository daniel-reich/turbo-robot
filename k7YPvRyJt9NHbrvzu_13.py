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
    ans = 0
    for k2 in range(1 + score // 2):
        for k3 in range(1 + score // 3):
            for k6 in range(1 + score // 6):
                for k7 in range(1 + score // 7):
                    for k8 in range(1 + score // 8):
                        if 2 * k2 + 3 * k3 + 6 * k6 + 7 * k7 + 8 * k8 == score:
                            ans += 1
    return ans

