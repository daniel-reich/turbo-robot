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
    return sum(2 * n2 + 3 * n3 + 6 * n6 + 7 * n7 + 8 * n8 == score
               for n2 in range(score // 2 + 1)
               for n3 in range((score - 2 * n2) // 3 + 1)
               for n6 in range((score - 2 * n2 - 3 * n3) // 6 + 1)
               for n7 in range((score - 2 * n2 - 3 * n3 - 6 * n6) // 7 + 1)
               for n8 in range((score - 2 * n2 - 3 * n3 - 6 * n6 - 7 * n7)
                               // 8 + 1))

