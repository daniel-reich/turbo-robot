"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

def prime_divisors(num):
    lst = []
    lst1 = []
    c = 0
    for i in range(2, int(num)):
        if num % i == 0:
            lst.append(i)
    for j in lst:
        if prime(j) or j == 2:
            lst1.append(j)
    return lst1
​
def prime(num):
    if num % 2 == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

