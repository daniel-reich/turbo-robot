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
    n = len(asteroids)
    if n < 2:
        return asteroids
    crashed = {i: False for i in range(n)}
    current = other = 1 if asteroids[0] < 0 else 0
    while current < n:
        direction = asteroids[current] > 0
        other += 1 if direction else -1
        if other >= n:
            break
        elif other < 0:
            current += 1
            other = current
            continue
​
        other_direction = asteroids[other] > 0
​
        if crashed[current]:
            current += 1
            other = current
        elif other_direction == direction and other_direction:
            current = other
        elif other_direction != direction:
            if not crashed[other]:
                mass = abs(asteroids[current])
                other_mass = abs(asteroids[other])
                if mass > other_mass:
                    crashed[other] = True
                elif mass < other_mass:
                    crashed[current] = True
                    current += 1
                    other = current
                else:
                    crashed[current] = True
                    crashed[other] = True
                    current += 1
                    other = current
            elif direction:
                current += 1
                other = current
    return [asteroids[i] for i in range(n) if not crashed[i]]

