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
  done = False
  print(asteroids)
  while not done:
    original_size = len(asteroids)
    print('Original Size: ' + str(original_size))
    for count, asteroid in enumerate(asteroids):
      if asteroid < 0:
        # Something to the left?
        if count > 0:
          # Evaluate
          if asteroids[count - 1] < 0:
            continue
          elif abs(asteroid) > asteroids[count - 1]:
            del asteroids[count - 1]
          elif abs(asteroid) == asteroids[count - 1]:
            del asteroids[count]
            del asteroids[count - 1]
          else:
            del asteroids[count]
          print(asteroids)
          break
          
    if original_size == len(asteroids):
      print('Final Size: ' + str(len(asteroids)))
      done = True
      
  return asteroids

