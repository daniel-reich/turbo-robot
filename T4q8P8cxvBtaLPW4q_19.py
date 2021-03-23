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
def is_prime(n):
    i=2
    while(i<=math.sqrt(n)):
        if n%i ==0 and n!=i:
            return False
            break
        i+=1
    return True
​
def extract_primes(num):
    str1=str(num)
    lst=[]
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            str2=str1[i:j+1]
            if str2[:1] == '0' or str2[-1] =='0':
                str2=1
            if is_prime(int(str2)) and int(str2)!=1 and int(str2)!=0:
                lst.append(int(str2))
    lst.sort()
    return lst

