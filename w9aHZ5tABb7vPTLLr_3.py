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

import math
​
def binomial_coefficient(n, k):
    return 0 if k > n else math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
​
def lucky_ticket(n_digits):
    ans = 0
    n = n_digits // 2
    sign = -1
    for q in range(n):
        sign *= -1
        ans += binomial_coefficient(2 * n, q) * sign * binomial_coefficient(11 * n - 10 * q - 1, 2 * n - 1)
    return ans

