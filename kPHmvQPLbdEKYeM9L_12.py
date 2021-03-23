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
        res = []
        stack = [] 
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                killed = False
                while len(stack) > 0:
                    last = stack[-1]
                    if abs(asteroid) >= last:
                        stack.pop(-1)
                        if abs(asteroid) == last:
                            killed = True
                            break                        
                    else:
                        break
                if not killed and len(stack) == 0:
                    res.append(asteroid)
        return res + stack

