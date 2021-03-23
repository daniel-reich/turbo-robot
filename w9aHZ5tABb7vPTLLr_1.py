"""


Create a function that counts how many n-digit numbers have the same sum of
the first half and second half of the digits (“lucky” numbers). The number `n`
is **even**. For example, for `n = 6`, the numbers "001010", "112220",
"000000" are lucky.

### Examples

    lucky_ticket(2) ➞ 10
    
    lucky_ticket(4) ➞ 670
    
    lucky_ticket(12) ➞ 39581170420

### Notes

  * The function should be really efficient.
  * The runtime increases 10 fold per test. Just for information: my solution takes 6 seconds, which is still under the server time-limit, so you are good to go.

"""

def lucky_ticket(n_digits):
  gen = [1 for i in range(10)]
  power = [1]
  for i in range(n_digits):
    power = poly_mult(power,gen)
  return power[9*n_digits//2]
​
​
def poly_mult(c1, c2):
    n, m = len(c1), len(c2)
    prod = []
    for k in range(n+m-1):
        prod.append(sum(c1[i]*c2[k-i] for i in range(max(0, k-m+1), min(n, k+1))))
    return prod

