"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(seq):
    '''
    Returns True if seq has a sequence of at least 2 ascending & consecutive
    numbers.
    '''
    size = len(seq)
​
    for j in range(1, size//2 + 1):
        if size % j == 0:
            if all([int(seq[i:i+j]) == int(seq[i-j:i]) + 1 for i in range(j, size, j)]):
                return True
​
    return False

