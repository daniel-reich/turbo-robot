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
  #base case
  if(n <= 1):
    return 1
    
  #inductive case
  else:
    return n * factorial(n-1)

