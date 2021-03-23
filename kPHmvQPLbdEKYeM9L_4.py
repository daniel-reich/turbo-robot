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
    left = []
    while len(asteroids) > 0 and asteroids[0] < 0:
        left.append(asteroids.pop(0))
    change = True
    while change and len(asteroids) >= 2:
        change = False
        for i in range(len(asteroids) - 1):
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                # collision
                change = True
                if asteroids[i] == -asteroids[i+1]:
                    # both will be destroyed:
                    asteroids.pop(i)
                    asteroids.pop(i)
                elif asteroids[i] < -asteroids[i+1]:
                    asteroids.pop(i)
                else:
                    asteroids.pop(i+1)
                break
        while len(asteroids) > 0 and asteroids[0] < 0:
            left.append(asteroids.pop(0))
    ans = left + asteroids
    return ans

