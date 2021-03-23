"""


Given a list of 10 numbers, return the **maximum possible total** made by
summing just **5 of the 10 numbers**.

### Examples

    max_total([1, 1, 0, 1, 3, 10, 10, 10, 10, 1]) ➞ 43
    
    max_total([0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) ➞ 100
    
    max_total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 40

### Notes

You can select any 5 numbers from the given array to form maximum possible
total.

"""

def max_total(nums):
    new_list = sorted(nums)
    return sum(new_list[5:])
​
print(max_total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

