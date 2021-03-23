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
    if asteroids == []:
        return []
    result_lst = [asteroids[0]]
    for i in range(1, len(asteroids)):
        if asteroids[i] < 0 and asteroids[i - 1] < 0:
            result_lst.append(asteroids[i])
        elif asteroids[i] > 0 and asteroids[i - 1] > 0:
            result_lst.append(asteroids[i])
        elif asteroids[i-1] < 0 and asteroids[i] > 0:
            result_lst.append(asteroids[i])
        elif asteroids[i-1] > 0 and asteroids[i] < 0:
            if abs(asteroids[i]) > asteroids[i-1]:
                result_lst.pop()
                result_lst.append(asteroids[i])
            elif abs(asteroids[i]) == asteroids[i - 1]:
                result_lst.pop()
    if result_lst == [] or result_lst == asteroids:
        return result_lst
    return asteroid_collision(result_lst)

