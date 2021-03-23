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
    '''
    Returns asteroids with any exploded ones removed, as per instructions.
    '''
    def winner(ast, rights):
        '''
        Returns True if ast survives collision with rights and updates
        rights appropriately
        '''
        for i in range(len(rights)-1, -1, -1):
            if ast > rights[i]:
                del rights[i]  # left moving asteroid destroyed this one
            elif ast == rights[i]:
                del rights[i]
                return False   # both destroyed
            else:
                return False   # ast destroyed
​
        return True  # ast survived
            
    rights, survivors = [], []
    for ast in asteroids:
        if ast < 0:
            if winner(abs(ast), rights):
                survivors.append(ast)
        else:  # moving right
            rights.append(ast)
​
    return survivors + rights

