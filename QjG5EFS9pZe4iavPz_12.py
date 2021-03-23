"""


The Fibonacci sequence is a classic use case for recursive functions since the
value of the sequence at a given index is dependent on the sum of the last two
values. **However** , the recursion tree created by solving the Fibonacci
sequence recursively can grow quite fast. Therefore it can be important to
think about the implications of running a function recursively. Depending on
the size of `n` needed and the capabilities of the system in question you
might want to take a **different approach**.

Write a **non-recursive function** that takes an integer `n` and returns the
Fibonacci sequence's value at index `n`.

### Examples

    fib(6) ➞ 8
    # 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
    
    fib(1) ➞ 1
    
    fib(2) ➞ 1

### Notes

Inputs will be whole numbers >= 0

"""

def fib(n):
  b =1
  a = 1
  d = 0
  if n==1 or n==2 :
    return 1
  if n==0 :
    return 0
  else :
    for i in range(3 , n+1):
      d = a
      a= b
      b = b + d
    return b

