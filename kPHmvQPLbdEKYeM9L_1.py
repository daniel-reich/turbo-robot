"""


You are given a list `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the `asteroids` after all collisions. If two `asteroids`
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

### Examples

    asteroid_collision([-2, -1, 1, 2]) ➞ [-2, -1, 1, 2]
    
    asteroid_collision([-2, 1, 1, -2]) ➞ [-2, -2]
    
    asteroid_collision([1, 1, -2, -2]) ➞ [-2, -2]
    
    asteroid_collision([10, 2, -5]) ➞ [10]
    
    asteroid_collision([8, -8]) ➞ []

### Notes

BONUS: Use only one loop (either `for` or `while`).

"""

def asteroid_collision(asts):
  if len(asts)<2 : return asts
  if asts[0]<0:
    return [asts[0]] + asteroid_collision(asts[1:])
  else:
    meh = asteroid_collision(asts[1:])
    if meh[0]>0: return [asts[0]] + meh
    if asts[0]+meh[0] < 0: return meh
    if asts[0]+meh[0] == 0: return meh[1:]
    if asts[0]+meh[0] > 0: return asteroid_collision([asts[0]]+meh[1:])

