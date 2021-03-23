"""


Create a function that takes a list of numbers and returns the **second
largest** number.

### Examples

    second_largest([10, 40, 30, 20, 50]) ➞ 40
    
    second_largest([25, 143, 89, 13, 105]) ➞ 105
    
    second_largest([54, 23, 11, 17, 10]) ➞ 23

### Notes

There will be at least two numbers in the list.

"""

def second_largest(lst):
    return sorted(lst)[-2]

