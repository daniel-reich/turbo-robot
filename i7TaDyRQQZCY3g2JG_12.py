"""


Given a list of integers, create a function that will find the **smallest**
positive integer that is evenly divisible by all the members of the list. In
other words, find the least common multiple (LCM).

### Examples

    lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520
    
    lcm([5]) ➞ 5
    
    lcm([5, 7, 11]) ➞ 385
    
    lcm([5, 7, 11, 35, 55, 77]) ➞ 385

### Notes

N/A

"""

def lcm(n):
    x=n[0]
    for i in n[1:]:
        if x > i: 
            s = i 
        else: 
            s = x 
        for y in range(1, s+1): 
            if((x % y == 0) and (i % y == 0)): 
                gcd = y
        x = x*i//gcd   
    return x

