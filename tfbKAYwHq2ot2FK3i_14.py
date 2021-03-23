"""


Let's define a non-repeating integer as one whose digits are all distinct.
97653 is non-repeating while 97252 is not (it has two 2's). Among the binary
numbers, there are only two positive non-repeating integers: 1 and 10. Ternary
(base 3) has ten: 1, 2, 10, 20, 12, 21, 102, 201, 120, 210.

Write a function that has as it's argument the base or radix and returns the
number of non-repeating positive integers in that base.

### Examples

    non_repeats(2) ➞ 2
    
    non_repeats(4) ➞ 48
    
    non_repeats(5) ➞ 260
    
    non_repeats(6) ➞ 1630

### Notes

Assume a radix of 1 is not legitimate.

"""

from math import factorial
​
def non_repeats(num):
    # Start by calculating the total valid combinations of numbers
    # Total = n!/(n-i)!*(n-i), where n is the number given and i is the size of a 
    # sliding window inside the list of numbers.
    
    # Subtract the invalid numbers starting with 0 from all combinations. 
    # Zeros = (n-1)!/(n-i-1)!
    
    total = 0
    zeros = 0
    for i in range(num):
        combinations = factorial(num)//factorial(num-i)*(num-i)
        invalid = factorial(num-1)//factorial(num-i-1)
        total += combinations
        zeros += invalid
    
    return total-zeros

