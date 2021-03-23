"""


You are given a number `n`. Determine whether `n` has exactly **3 divisors**
or not.

### Examples

    is_exactly_three(4) ➞ True
    # 4 has only 3 divisors: 1, 2 and 4
    
    is_exactly_three(12) ➞ False
    # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    
    is_exactly_three(25) ➞ True
    # 25 has only 3 divisors: 1, 5, 25

### Notes

1 ≤ n ≤ 10^12

"""

def divisors(n):
  yield 1
  yield n
  i = 2
  while i < n//i:
    if not n%i:
      yield i
      yield n//i
    i+=1
  if i**2==n: yield i
​
def is_exactly_three(n):
  return len(list(divisors(n)))==3
