"""


Given a positive integer `n`, compute the nth term in the Fibonacci sequence.
For those of you that have been living under a rock in the mathematical world,
here's the definition:

  * The first and second terms are 1.
  * nth term is the (n-1)th term + the (n-2)th term. So the 3rd term is the 1st term + the 2nd term, the 4th term is the 3rd term + the 2nd term, etc.

Thus the sequence looks like this: 1, 1, 2, 3, 5, 8, 13, 21, ...

### Examples

    fibo(1) ➞ 1
    
    fibo(2) ➞ 1
    
    fibo(3) ➞ 2
    
    fibo(6) ➞ 8
    
    fibo(30) ➞ 832040

### Notes

N/A

"""

def calc(num):
    if num == 0:
        return (0, 1)
    elif num == 1:
        return (1, 1)
    else:
        a, b = calc(num // 2)
        p = a * (2 * b - a)
        q = b * b + a * a
        return (p, q) if num % 2 == 0 else (q, p + q)
​
def fibo(num):
    if num >= 0:
        return calc(num)[0]
    else:
        return -calc(-num)[0] if num % 2 ==0 else calc(-num)[0]

