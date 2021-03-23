"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

def prime(integer):
    for number in range(2,(integer//2)+1):
        if integer%number == 0:
            return False
    if integer <= 1:
        return False
    return True
​
def prime_numbers(ranger):
    counter = 0
    for i in range(ranger):
        if prime(i):
            counter += 1
            
    return counter

