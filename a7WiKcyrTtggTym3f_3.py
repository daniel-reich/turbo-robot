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

def gcd(a,b):
  if b==0:
    return a
  return gcd(b, a%b)
  
def lcm(a, b):
  return gcd(a,b)*(a//gcd(a,b))*(b//gcd(a,b))

