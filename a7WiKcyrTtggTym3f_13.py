"""


Create a function that takes two numbers as arguments and return the LCM of
the two numbers.

### Examples

    lcm(3, 5) ➞ 15
    
    lcm(14, 28) ➞ 28
    
    lcm(4, 6) ➞ 12

### Notes

  * Don't forget to return the result.
  * You may want to use the GCD function to make this a little easier.
  * LCM stands for least common multiple, the smallest multiple of both integers.

"""

def lcm(a, b):
    num = 0
    for n in range(2, a*b+1):
        if n % a == 0 and n % b == 0:
            num = n
            break
    return num

