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

def lcm(nums):
    if len(nums) ==1:
        return nums[0]
    nums.sort()
    maxnum = nums[-1]
    secondmaxnum = nums[-2] 
    product = 1
    for i in nums:
        product *= i
        
    if maxnum - secondmaxnum ==1:
        return int(product/2)
​
    for i in range(maxnum, product+1, maxnum):
        divisible = True
        for j in nums:
            if i % j != 0:
                divisible = False
​
        if divisible:
            return i

