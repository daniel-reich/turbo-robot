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
    while i + 1 < len(asteroids):
        a, b = asteroids[i], asteroids[i + 1]
        if a > 0 and b < 0:
            i = -1
            if a + b == 0:
                asteroids.remove(a)
                asteroids.remove(b)
            else:
                if abs(a) > abs(b):
                    asteroids.remove(b)
                else:
                    asteroids.remove(a)
        i += 1
    return asteroids

