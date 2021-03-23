"""


Create a function that takes a list and returns the sum of all numbers in the
list.

### Examples

    get_sum_of_elements([2, 7, 4]) ➞ 13
    
    get_sum_of_elements([45, 3, 0]) ➞ 48
    
    get_sum_of_elements([-2, 84, 23]) ➞ 105

### Notes

N/A

"""

get_sum_of_elements=lambda l:sum(i for i in l)

