"""


A Fibonacci Word is a specific sequence of binary digits (or symbols from any
two-letter alphabet). The Fibonacci Word is formed by repeated concatenation
in the same way that the Fibonacci numbers are formed by repeated addition.

Create a function that takes a number `n` as an argument and returns the first
`n` elements of the Fibonacci Word sequence.

If `n < 2`, the function must return `"invalid"`.

### Examples

    fibo_word(1) ➞ "invalid"
    
    fibo_word(3) ➞ "b, a, ab"
    
    fibo_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"

### Notes

N/A

"""

def fibo_word(n, f=['b', 'a'], i=0):
  if n < 2: return 'invalid'
  if n == i+2: return ', '.join(f)
  return fibo_word(n, f+[f[i+1]+f[i]], i+1)

