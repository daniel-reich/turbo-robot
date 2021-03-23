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

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
        
def lcm_cal(a,b):
    return a*b//gcd(a,b)    
def lcm(nums):
    lcm = 1
    for i in range(0,len(nums)):
        lcm = lcm_cal(lcm,nums[i])
    return lcm

