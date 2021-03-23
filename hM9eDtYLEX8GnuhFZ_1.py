"""


A simple random number generator or, as more properly called, a linear
congruential generator can be demonstrated by the equation `x1 =
(a*x0+1)%65535`. `a`, `x0`, and `x1` are non-negative integers less than
`65535`. The equation is seeded with `x0`. The first number generated, `x1`,
is then used as the seed for the next round and so on. If we choose `a=7` and
`x0=12345` the first 5 numbers generated are 20881, 15098, 40152, 18925, 1406.

Since such generators are used in games of chance and online gambling, it
would be to one's benefit if the next "random" number to be generated could be
predicted. Devise a function that takes 2 random numbers that were
sequentially generated by the above equation and returns the next number to be
generated. The value of `a` will be different for all test cases and is not
given. The initial seed, `x0=12345`, is the same for all test cases. If the
answer cannot be determined, return `None`.

### Examples

    random([1, 1]) ➞ 1
    # a=0
    
    random([12347, 12348]) ➞ 12349
    # a=1
    
    random([5806, 9802]) ➞ 37768
    # a=171
    
    random([48028, 25564]) ➞ 12565
    # a=21
    
    random([36020, 26121]) ➞ None
    # a=77
    
    random([39000, 24931]) ➞ None
    # a=4

### Notes

  * I believe test cases with result `None` cannot be solved. If you can figure out a method to solve them please post a comment.
  * All test cases were taken from the first 10 numbers generated.

"""

from fractions import gcd
def random(lst):
    fr, lr = lst 
    if lr == fr: return lr
    m, n = 65535, 0
    while True:
        a = (lr - 1  +  m * n) / fr
        if a % 1 == 0:
            a = int(a)
            break
        n += 1
    return None if a + m // gcd(m, fr) < m else (a * lr + 1) % m

