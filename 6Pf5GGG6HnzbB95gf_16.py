"""


Create a function that finds each **factor** of a given number `n`. Your
solution should return a list of the number(s) that meet this criteria.

### Examples

    find_factors(9) ➞ [1, 3, 9]
    # 9 has three factors 1, 3 and 9
    
    find_factors(12) ➞ [1, 2, 3, 4, 6, 12]
    
    find_factors(20) ➞ [1, 2, 4, 5, 10, 20]
    
    find_factors(0) ➞ []
    # 0 has no factors

### Notes

Return an **empty list** if the given number is less than `1`.

"""

def find_factors(n):
  return [i for i in range(1,n+1) if n % i == 0]

