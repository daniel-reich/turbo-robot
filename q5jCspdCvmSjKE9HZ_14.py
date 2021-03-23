"""


Create a function that takes a list of more than three numbers and returns the
**Least Common Multiple** (LCM).

### Examples

    lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520
    
    lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340
    
    lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760

### Notes

The LCM of a list of numbers is the smallest positive number that is divisible
by each of the numbers in the list.

"""

import functools
​
def gcf(num1,num2):
  factors = list(filter(lambda x: num1 % x == 0 and num2 % x == 0,range(1,num1+1)))
  return factors[-1]
def lcm(num1,num2):
  gcd = gcf(min(num1,num2),max(num1,num2))
  return (num1 // gcd) * num2
        
def lcm_of_list(numbers):
  return functools.reduce(lambda x,y: lcm(x,y),numbers)

