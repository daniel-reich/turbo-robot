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
    qtd = len(asteroids)
    remain = [asteroids[0]]
    add_ast = remain.append
    rem_ast = remain.pop
    pos = 1
    while pos < qtd:
        ast = asteroids[pos]
        if ast > 0:
            add_ast(ast)
            pos += 1
        else:
            if remain[-1] < 0:
                add_ast(ast)
                pos += 1
            else:
                if remain[-1] < abs(ast):
                    rem_ast()
                    if not remain:
                        add_ast(ast)
                        pos += 1
                elif remain[-1] == abs(ast):
                    rem_ast()
                    pos += 1
                else:
                    pos += 1
    return remain

