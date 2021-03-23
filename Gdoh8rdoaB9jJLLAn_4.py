"""


Create a function that takes an expression `exp` and an upper limit `i` as
arguments and returns the sum of that expression up to the i'th term (recall
sigma from math class).

### Examples

    summation("n", 10) ➞ 55
    
    summation("1/n", 50) ➞ 4.5
    
    summation("n**n", 6) ➞ 50069

### Notes

  * Assume the lower limit is `i = 1`.
  * Round your answer to the nearest tenth.

"""

def summation(exp, n):
  if exp == '0':
    return 0
  def f(s,n):
    if n == 0:
      return round(s,1)
    return f(s+eval(exp.replace('n',str(n))),n-1)
  return f(0,n)

