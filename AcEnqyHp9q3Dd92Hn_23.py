"""


Given a string of numbers separated by a _comma and space_ , return the
product of the numbers.

### Examples

    multiply_nums("2, 3") ➞ 6
    
    multiply_nums("1, 2, 3, 4") ➞ 24
    
    multiply_nums("54, 75, 453, 0") ➞ 0
    
    multiply_nums("10, -2") ➞ -20

### Notes

Bonus: Try to complete this challenge in **one line**!

"""

def multiply_nums(nums):
    nums = "".join(nums.split())
    nums = nums.split(',')
    print(nums)
    a = [int(i) for i in nums]
    #print(a)
    p = 1
    for i in a:
        p *= i
    return p

