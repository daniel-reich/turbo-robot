"""
Create a function that takes in a positive integer _n_ and returns the
**simplified square root** of _n_ as a tuple of positive integers ( _a_ , _b_
), where _a_ ⋅sqrt( _b_ ) = sqrt( _n_ ) and _b_ is as small as possible.

### Examples

    simplify_sqrt(72) ➞ (6, 2)
    
    simplify_sqrt(160) ➞ (4, 10)
    
    simplify_sqrt(36) ➞ (6, 1)
    
    simplify_sqrt(35) ➞ (1, 35)

A common way to simplify square roots is to repeatedly factor out perfect
squares from the number underneath the square root. For example, if you need
to simply sqrt(72), you can factor out perfect squares from 72 according to
the following process:

    sqrt(72)

72 is divisible by 4, so factor 4 out of 72:

    sqrt(4⋅18)

The perfect square 4 can now be square rooted and pulled out of the square
root:

    2⋅sqrt(18)

Now repeat the process until no further perfect squares can be factored out.
18 is divisible by 9, so factor it out:

    2⋅sqrt(9⋅2)

Pull the 9 out, square root it, and simplify:

    2⋅3⋅sqrt(2)
    = 6⋅sqrt(2)

2 does not have any perfect square factors other than 1, so 6⋅sqrt(2) is the
simplest form of sqrt(72). The function would therefore return the tuple (6,
2).

This is only one approach to solving this problem; there are probably other
ways that are simpler/faster than this method. Feel free to use any method you
want.

### Notes

  * If _n_ is a perfect square, _b_ should be 1.
  * If _n_ has no perfect square factors (other than 1), _a_ should be 1.

"""

def simplify_sqrt(n):
    a = 1
    b = 1
​
    if natural_sqrt(n):
        return (natural_sqrt(n), 1)
​
    for i in range(1, int(n/2+1)):
        if n%i==0 and natural_sqrt(i):
            a = natural_sqrt(i)
            b = n/i
​
    return (a, int(b))
​
def natural_sqrt(n):
    if n == 1:
        return 1
        
    for i in range(1, n//2+1):
        if i*i == n:
            return i
    
    else: return False

