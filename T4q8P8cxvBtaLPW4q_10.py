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

import math
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
#return all possible strings 
#like abcde 
#a, b, c, d, e, ab, bc, cd, de, abc, bcd, cde, abcd, bcde
def extract(num, length):
    out = []
    num = str(num)
    limit = len(num) - length 
    for i in range(limit + 1):
        out.append(num[i:i + length])
    return out
def extract_primes(num):
    num = str(num)
    output = []
    primes = []
    for i in range(1, len(num) + 1):
        output.append(extract(num, i))
    print(output)
    for lst in output:
        #print(lst)
        
        for e in lst:
            if e[0] == '0':
                continue
            if isPrime(int(e)):
                primes.append(int(e))
    return sorted(primes)
​
def remDupe(lst):
    for e in range(len(lst)):
        if lst.count(lst[e])  == 1:
            if e == len(lst) - 1:
                return lst
            #print(lst)
            continue
        else:
            del lst[e]
            remDupe(lst)
    return lst

