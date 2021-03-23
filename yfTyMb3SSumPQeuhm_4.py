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
      
    F = [[1, 1], 
         [1, 0]] # Matrix
         
    if (n == 0): 
        return "You are gay"
    power(F, (n-1)) 
          
    return F[0][0] 
      
def multiply_matrices(F, M): 
      
    bottom_left = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    top_left = (F[0][0] * M[0][1] + 
         F[0][1] * M[1][1]) 
    bottom_right = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    top_right = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = bottom_left 
    F[0][1] = top_left
    F[1][0] = bottom_right
    F[1][1] = top_right
          
def power(F, n): 
  
    if n==0 or n == 1: 
        return
    M = [[1, 1], 
         [1, 0]]
          
    power(F, (n//2)) 
    multiply_matrices(F, F) 
          
    if n % 2 != 0: 
        multiply_matrices(F, M)

