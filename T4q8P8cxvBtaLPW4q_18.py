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

def is_prime (n):
  if n == 1 or n == 0 :
    return False
  for i in range (2,n):
    if n%i == 0:
      return False
  return True
​
​
​
​
def extract_primes (num):
  num_list = list (str(num))
  num_list.reverse()
  prime_list = [ ]
  for len_num in range (1,len (num_list)+1):
​
    for i in range (len(num_list)-len_num + 1 ):
      c = 0 
      decimal_num = 0 
      while c!= (len_num ):
        decimal_num += (int (num_list[i+c]))*10**c
        mem = num_list[i+c]
        c+=1 
        
​
      if is_prime (decimal_num) and int (mem) != 0:
        prime_list.append (decimal_num)
  prime_list.sort()
  return prime_list

