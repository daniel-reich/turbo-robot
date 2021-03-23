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

points = [2,3,6,7,8]
def football(score, series = [[]], pointer = 0):
  if pointer == len(points):
    return len([serie for serie in series if sum(serie) == score])
  point = points[pointer]
  limit = score // point + 1
  series = [serie + [point]*i for i in range(limit) for serie in series]
  return football(score, series, pointer +1)

