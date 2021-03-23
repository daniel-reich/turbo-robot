"""


Write a function that returns `True` if an integer can be expressed as a power
of base value 2 and `False` otherwise.

### Examples

    power_of_two(32) ➞ True
    
    power_of_two(1) ➞ True
    
    power_of_two(18) ➞ False

### Notes

N/A

"""

def power_of_two(num): #mediocre code way
    if num == 0:
        return False
    elif num == 1 or num == 2:
        return True
    n, p = 2, 1
    while n < num:
        n **= p
        if n == num:
            return True
        elif n > num:
            return False
        n = 2
        p += 1
    return False
    
def power_of_two(num):
    return num != 0 and (num & (num - 1) == 0)

