"""


Create a function that takes an integer `n` and returns the **factorial of
factorials**. See below examples for a better understanding:

### Examples

    fact_of_fact(4) ➞ 288
    # 4! * 3! * 2! * 1! = 288
    
    fact_of_fact(5) ➞ 34560
    
    fact_of_fact(6) ➞ 24883200

### Notes

N/A

"""

def fact_of_fact(n):
  x = 1
  b = 1
  for i in range(n):
    for m in range(n - i):
      if m == (n - 1):
        break
      x = x * ((n - i) - m)
    b = b * x
    x = 1
  return(b)

