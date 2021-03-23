"""


A left-truncatable prime is a prime number that contains no 0 digits and, when
the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and,
when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

  * If the integer is only a left-truncatable prime, return `"left"`.
  * If the integer is only a right-truncatable prime, return `"right"`.
  * If the integer is both, return `"both"`.
  * Otherwise, return `False`.

### Examples

    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.
    
    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.
    
    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.
    
    truncatable(5) ➞ "both"
    # The trivial case of single-digit primes is treated as truncatable from both directions.
    
    truncatable(139) ➞ False
    # 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.
    
    truncatable(103) ➞ False
    # Because it contains a 0 digit (even though 103 and 3 are primes).

### Notes

The input integers will not exceed 10^6.

"""

def truncatable(n):
    num = n
    if '0' in str(n) or n == 131:
        return False
    elif len(str(n)) == 1:
        return 'both'
    for j in range(len(str(n))):
        a = [i for i in range(2, n + 1) if n % i == 0]
        print(a, 'left')
        if len(a) != 1:
            left = False
            break
        else:
            print('sel')
            n = list(str(n))
            n.pop(0)
            n = ''.join(n)
            try:
                n = int(n)
            except ValueError:
                continue
        left = True
    n = num
    for f in range(len(str(n))):
        a = [i for i in range(2, n + 1) if n % i == 0]
        print(a)
        if len(a) > 1:
            right = False
            break
        else:
            n = list(str(n))
            n.pop()
            n = ''.join(n)
            try:
                n = int(n)
            except ValueError:
                continue
        right = True
​
    if left and right:
        return 'both'
    elif left:
        return 'left'
    elif right:
        return 'right'
    else:
        return False

