"""


Given a list of integers, create a function that will find the **smallest**
positive integer that is evenly divisible by all the members of the list. In
other words, find the least common multiple (LCM).

### Examples

    lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520
    
    lcm([5]) ➞ 5
    
    lcm([5, 7, 11]) ➞ 385
    
    lcm([5, 7, 11, 35, 55, 77]) ➞ 385

### Notes

N/A

"""

def prime_factors(n):
    factors = []
    for i in range(2, int(n ** .5) + 1):
        while not n % i:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
​
​
def lcm(nums):
    factors = []
    for num in nums:
        if 1 < num < 4:
            factors.append([num])
        else:
            factors.append(prime_factors(num))
    while len(factors) > 1:
        for x in factors[0]:
            if x in factors[1]:
                factors[1].remove(x)
        factors[0] += factors[1]
        factors.pop(1)
    total = 1
    for factor in factors[0]:
        total *= factor
    return total

