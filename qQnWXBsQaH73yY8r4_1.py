"""


The Kempner Function, applied to a composite number, permits to find the
smallest integer greater than zero whose factorial is exactly divided by the
number.

    kempner(6) ➞ 3
    
    1! = 1 % 6 > 0
    2! = 2 % 6 > 0
    3! = 6 % 6 === 0
    
    kempner(10) ➞ 5
    
    1! = 1 % 10 > 0
    2! = 2 % 10 > 0
    3! = 6 % 10 > 0
    4! = 24 % 10 > 0
    5! = 120 % 10 === 0

A Kempner Function applied to a prime will always return the prime itself.

    kempner(2) ➞ 2
    kempner(5) ➞ 5

Given an integer `n`, implement a Kempner Function.

### Examples

    kempner(6) ➞ 3
    
    kempner(10) ➞ 5
    
    kempner(2) ➞ 2

### Notes

  * Try solving this recursively, with an approach oriented to higher-order functions.
  * If you need to get more confident with recursion and factorials, try [this challenge](https://edabit.com/challenge/wRf3e8T3vQpG7SmjP).

"""

from math import factorial as f
def kempner(n, i=1):
    return kempner(n, i +1) if f(i)%n else i

