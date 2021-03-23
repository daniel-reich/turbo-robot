"""


Write a function that calculates the **factorial** of a number
**recursively**.

### Examples

    factorial(5) ➞ 120
    
    factorial(3) ➞ 6
    
    factorial(1) ➞ 1
    
    factorial(0) ➞ 1

### Notes

N/A

"""

def factorial(n):
  aux = n
  n = n-1
  if(n > 0):
    aux = aux * factorial (n)
  else:
    aux = 1;
  return aux

