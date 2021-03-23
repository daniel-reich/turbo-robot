"""


A **pronic** number (or otherwise called as **heteromecic** ) is a number
which is a _product of two consecutive integers_ , that is, a number of the
form `n(n + 1)`. Create a function that determines whether a number is pronic
or not.

### Examples

    is_heteromecic(0) ➞ True
    # 0 * (0 + 1) = 0 * 1 = 0
    
    is_heteromecic(2) ➞ True
    # 1 * (1 + 1) = 1 * 2 = 2
    
    is_heteromecic(7) ➞ False
    
    is_heteromecic(110) ➞ True
    # 10 * (10 + 1) = 10 * 11 = 110
    
    is_heteromecic(136) ➞ False
    
    is_heteromecic(156) ➞ True

### Notes

  * You are expected to solve this challenge via **recursion**.
  * You can check on the **Resources** tab for more details about _recursion_.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/Rbs2G5PaJtmYdLTJM).

"""

def is_heteromecic(n, test = 0):
  if n==test*(test+1): return True
  if test>int(n**.5): return False
  return is_heteromecic(n, test+1)
  # yet again, I'd hardly call this recursion...

