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

def football_score_backtracking(cur, lst, result, target, index):
    if sum(cur) == target:
        result.append(cur[:])
    if sum(cur) > target:
        return
    else:
        for i in range(index, len(lst)):
              cur.append(lst[i])
              football_score_backtracking(cur, lst, result, target, i)
              cur.pop()
    return result
​
def football(score):
    return len(football_score_backtracking([], [2, 3, 6, 7, 8], [], score, 0))

