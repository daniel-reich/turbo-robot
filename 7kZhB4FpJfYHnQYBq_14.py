"""


Create a function that takes an array of three numbers and returns the **Least
Common Multiple** (LCM).

The LCM is the smallest positive number that is a multiple of two or more
numbers. In our case, we are dealing with three numbers.

  * Multiples of 3 are: 3, 6, 9, 12, and so on.
  * Multiples of 4 are: 4, 8,12, and so on.
  * Multiples of 12 are: 12, and so on.

Thus, the least common multiple of 3, 4, and 12 is 12.

### Examples

    lcm_three([5, 7, 13]) ➞ 455
    
    lcm_three([104, 105, 107]) ➞ 1168440
    
    lcm_three([19, 47, 43]) ➞ 38399

### Notes

N/A

"""

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
​
​
def findlcm(a,b):
    return (a*b) // gcd(b % a, a)
​
def lcm_three(num):
    a = num[0]
    b = num[1]
​
    lcm = findlcm(a,b)
    for i in range(2,len(num)):
        lcm = findlcm(lcm,num[i])
​
    return lcm

