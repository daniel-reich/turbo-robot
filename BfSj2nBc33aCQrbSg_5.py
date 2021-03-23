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
    rightstring = str(n)
    leftstring = str(n)
    right = []
    left = []
    if '0' in rightstring:
        return False
    for x in str(n):
        right.append(all(int(rightstring) % j for j in range(2, int(int(rightstring)**0.5)+1)) and int(rightstring) > 1)
        left.append(all(int(leftstring) % j for j in range(2, int(int(leftstring)**0.5)+1)) and int(leftstring) > 1)
        rightstring = rightstring[:-1]
        leftstring = leftstring[1:]
    if left.count(True) == len(left) and right.count(True) == len(right):
        return 'both'
    if right.count(True) == len(right):
        return 'right'
    if left.count(True) == len(left):
        return 'left'
    else:
        return False

