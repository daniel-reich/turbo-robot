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

gcd = lambda x,y: gcd(y,x%y) if y else x; lcm = lambda x,y: x*y/gcd(x,y)
lcm_of_list=lol=lambda n:lcm(lol(n[1:]),n[0]) if len(n)>1 else n[0]

