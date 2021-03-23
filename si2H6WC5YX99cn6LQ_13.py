"""


Write a function that finds the sum of the first `n` natural numbers. **Make
your function recursive.**

###  Examples

    sum_numbers(5) ➞ 15
    # 1 + 2 + 3 + 4 + 5 = 15
    
    sum_numbers(1) ➞ 1
    
    sum_numbers(12) ➞ 78

### Notes

  * Assume the input number is always positive.
  * Check the **Resources** tab for info on recursion.

"""

def sum_numbers(n):
    x = 0
    c = 0
    for i in range(n):
        x = x + (n-c)
        c+=1
    return x

