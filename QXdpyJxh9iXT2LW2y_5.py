"""


In mathematics, a semiprime is a natural number that is the product of two
prime numbers. The two primes in the product may equal each other, so the
semiprimes include the squares of prime numbers.

Create a function that takes a number `n` as an argument and returns two
lists, one list with all the semiprimes < `n` and the other with all the
semiprimes < `n` and that are not square numbers.

### Examples

    semiprimes(20) ➞ ([4, 6, 9, 10, 14, 15], [6, 10, 14, 15])
    
    semiprimes(157) ➞ ([4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 121, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155], [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155])
    
    semiprimes(1), ([], [])

### Notes

N/A

"""

import math 
def checkSemiprime(num): 
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            cnt += 1
        if cnt >= 2:  
            break
    if(num > 1): 
        cnt += 1
    return cnt == 2
def semi_prime(n): 
    if checkSemiprime(n) == True: 
        return n
def createSemiPrimeSieve(n): 
    v = [0 for i in range(n + 1)] 
    for i in range(1, n + 1): 
        v[i] = i 
    countDivision = [0 for i in range(n + 1)] 
    for i in range(n + 1): 
        countDivision[i] = 2
    for i in range(2, n + 1, 1): 
        if (v[i] == i and countDivision[i] == 2):
            for j in range(2 * i, n + 1, i): 
                if (countDivision[j] > 0): 
                    v[j] = int(v[j] / i)
                    countDivision[j] -= 1
    res = [] 
    for i in range(2, n + 1, 1):
        if (v[i] == 1 and countDivision[i] == 0): 
            res.append(i) 
    return res     
def semiprimes(n):        
    return ([i for i in range(1,n) if semi_prime(i)],createSemiPrimeSieve(n))

