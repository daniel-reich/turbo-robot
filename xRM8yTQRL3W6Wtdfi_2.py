"""


Create a function that returns the number of (real) solutions of
`ax^4+bx^2+c=0`. The function will take three arguments: `a` as the
coefficient of `x^4`, `b` as the coefficient of `x^2`, and `c` as the constant
term.

### Examples

    quartic_equation(1, -5, 4) ➞ 4
    
    quartic_equation(4, 3, -1) ➞ 2
    
    quartic_equation(1, 10, 9) ➞ 0

### Notes

Hint: Try substitution `t=x^2`.

"""

def quartic_equation(a, b, c):
  dis = (b**2 - 4*a*c)
  if dis < 0: return 0
  if dis == 0: return 0 if a*b <0 else 1 if a*b == 0 else 2
  n1, n2 = dis**0.5 - b, -dis**0.5 - b
  if n1 < 0 and n2 < 0: return 0
  if n1 > 0 and n2 > 0: return 4
  if n1 == 0: return 1 if n2 < 0 else 3
  if n2 == 0: return 1 if n1 < 0 else 3
  return 2

