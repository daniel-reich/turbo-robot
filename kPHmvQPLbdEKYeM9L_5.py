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

def asteroid_collision(asteroids):
  i = 0
  while i < len(asteroids)-1:
    if asteroids[i] > 0 and asteroids[i+1] < 0:
      if abs(asteroids[i]) < abs(asteroids[i+1]):
        asteroids.pop(i)
      elif abs(asteroids[i]) > abs(asteroids[i+1]):
        asteroids.pop(i+1)
      else:
        asteroids.pop(i)
        asteroids.pop(i)
      if i > 0:
        i -= 1
    else:
      i += 1
  return asteroids

