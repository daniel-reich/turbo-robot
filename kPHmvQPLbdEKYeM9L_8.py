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
        x = 0
        while x < len(asteroids) * 5:  # nah, efficiency bad
            for i in range(len(asteroids) - 1):
                as1 = asteroids[i];
                as2 = asteroids[i + 1]
                if as1 > 0 and as2 < 0:
                    if as1 > abs(as2):
                        asteroids.pop(i + 1)
                    elif as1 == abs(as2):
                        asteroids.pop(i)
                        asteroids.pop(i)
                    else:
                        asteroids.pop(i)
                    break
            x += 1
        return asteroids

