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
    new_nums = ""
    total = 1
​
    for char in nums:
        if char == ",":
            continue
        new_nums += char
​
    edited = new_nums.split()
    
    for number in edited:
        total *= int(number)
​
    return total

