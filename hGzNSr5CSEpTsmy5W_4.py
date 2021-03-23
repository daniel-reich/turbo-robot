"""


Create a function that subtracts 1 from `n` (unless it ends in 0) `k` number
of times. If `n` ends in `0`, remove the `0`.

To illustrate:

    n = 22
    k = 3

This means our number is 22 and we have to repeat the algorithm three times.
22 does not end in 0 so we continue subtracting 1.

    22 - 1 = 21
    k = 1
    21 - 1 = 20
    k = 2

Now 20 ends in 0, so we can remove it. We get 2; k = 3. The algorithm ends
there because we applied it three times.

    N:  K:
    22
    21  1
    20  2
    2   3

### Examples

    not_good_math(540, 5) ➞ 50
    
    not_good_math(1000000000, 9) ➞ 1
    
    not_good_math(42023110, 10) ➞ 4201

### Notes

Check resources!!

"""

def not_good_math(n,k):
  while k > 0:
      if n%10==0:
          n //= 10
      else:
          n -= 1
      k -= 1
  return n

