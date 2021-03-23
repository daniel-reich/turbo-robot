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
    while i < len(asteroids):
        if asteroids[i] > 0:
            if i + 1 < len(asteroids) and asteroids[i+1] < 0:
                s = asteroids[i] + asteroids[i+1]
                if s > 0: 
                    asteroids.pop(i+1)
                else:
                    asteroids.pop(i)
                    if s == 0: 
                        asteroids.pop(i)
                    i -= 1
                if i >= 0: continue
        i += 1
    return asteroids

