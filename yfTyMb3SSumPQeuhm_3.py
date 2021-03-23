"""


Write a function that efficiently calculates Fibonacci terms.

### Examples

    fibonacci(1) ➞ 1
    
    fibonacci(2) ➞ 1
    
    fibonacci(4) ➞ 3
    
    fibonacci(64) ➞ 10610209857723

### Notes

The input will always be a power of two.

"""

def fibonacci(n):
  return power_fib(len(bin(n))-3)
​
def power_fib(k):
  if k in power_fibs: return power_fibs[k]
  p,q = sq5_ap(k)
  power_fibs[k] = 1 + power_fib(k-1)**2*p//q
  return power_fibs[k]
​
def sq5_ap(k):
  if k in sq5_appr: return sq5_appr[k]
  p,q = sq5_ap(k-1)
  p,q = p**2+5*q**2, 2*p*q
  sq5_appr[k] = [p,q]
  return [p,q]
​
power_fibs = {0:1, 1:1, 2: 3, 3: 21}
sq5_appr = {3: [6016, 2688]}

