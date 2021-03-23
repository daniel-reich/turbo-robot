"""


Create a function to return the Nth number in the Fibonacci sequence as a
string.

### Examples

    fibonacci(10) ➞ "55"
    
    fibonacci(20) ➞ "6765"
    
    fibonacci(30) ➞ "832040"
    
    fibonacci(40) ➞ "102334155"
    
    fibonacci(50) ➞ "12586269025"
    
    fibonacci(60) ➞ "1548008755920"

### Notes

Your function is expected to calculate numbers greater than the 64-bit
unsigned integer limit where `n` can be as large as but not greater than 200.

"""

def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return str(a)

