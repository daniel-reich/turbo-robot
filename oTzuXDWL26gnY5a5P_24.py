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

def prime_numbers(x):
    primearray=[]
    for i in range(1, x):
        if checkprime(i) == True:
            primearray.append(i)
        else:
            continue
    return(len(primearray))
        
def checkprime(x):
    if x >= 2:
        for y in range(2, x):
            if not(x%y):
                return False
    else:
        return False
    return True

