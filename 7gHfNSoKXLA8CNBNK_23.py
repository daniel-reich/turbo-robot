"""


Create a function that takes a number `max_den` and returns the total number
of fully simplified proper fractions that exist with denominator less than or
equal to `max_den`.

You only need to return the number of fractions; **NOT the fractions
themselves**. In the examples below, I list the fractions simply for your
reference.

### Examples

    sim_prop_frac(10) ➞ 31
    # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1/8, 3/8, 5/8, 7/8, 1/9, 2/9, 4/9, 5/9, 7/9, 8/9, 1/10, 3/10, 7/10, 9/10
    
    sim_prop_frac(7) ➞ 17
    # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7

### Notes

A fully simplified proper fraction is a fraction where both the numerator and
denominator share no common factors besides 1 and the fraction is less than 1.

"""

def sim_prop_frac(n):
  gcd = lambda a, b: a if not b else gcd(b, a % b)
  return len(set(str(q//gcd(p, q))+'/'+str(p//gcd(p, q))
    for p in range(1, n+1) for q in range(1, p+1) if p != q))

