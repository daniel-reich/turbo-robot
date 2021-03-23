"""


Create a function that takes an integer argument and returns a list of prime
numbers found in the decimal representation of that number (not factors).

For example, `extract_primes(1717)` returns `[7, 7, 17, 17, 71]`.

The list should be in acending order. If a prime number appears more than
once, every occurance should be listed. If no prime numbers are found, return
an empty list.

### Examples

    extract_primes(1) ➞ []
    
    extract_primes(7) ➞ [7]
    
    extract_primes(73) ➞ [3, 7, 73]
    
    extract_primes(103) ➞ [3]
    
    extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]

### Notes

  * All test cases are positive real integers.
  * Some numbers will have leading zeros. For example, the number `103` contains the prime number `3`, but also contains `03`. These should be treated as the same number, so the result would simply be `[3]`.

"""

def is_prime(num):
  count = 0
  for i in range(1, num+1):
    if num % i == 0:
      count += 1
  return count == 2
​
def extract_primes(num):
  primes = []
  for i in range(len(str(num))):
    for j in range(i + 1, len(str(num))+1):
      if is_prime(int((str(num))[i:j])) and int((str(num))[i]) != 0:
        primes.append(int((str(num))[i:j]))
  return sorted(primes)

