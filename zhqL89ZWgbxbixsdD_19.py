"""


Create a **recursive** function that tests if a number is the exact upper
bound of the factorial of `n`. If so, return a list that contains the **exact
factorial bound** and `n`, or otherwise, the string `"Not exact!"`.

### Examples

    is_exact(6) ➞ [6, 3]
    
    is_exact(24) ➞ [24, 4]
    
    is_exact(125) ➞ "Not exact!"
    
    is_exact(720) ➞ [720, 6]
    
    is_exact(1024) ➞ "Not exact!"
    
    is_exact(40320) ➞ [40320, 8]

### Notes

  * It is expected from the challenge-takers to come up with a solution using the concept of **recursion** or the so-called **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or hasn't fully understood the concept behind it before taking up this challenge or unless otherwise.
  * There will be no exceptions to handle, all inputs are positive integers.
  * A non-recursive version of this challenge (of lesser difficulty and gives you the total liberty of not using the recursive approach) can be found in [here](https://edabit.com/challenge/f24TDCGbYRjGfALQp).

"""

def is_exact(n,new_n=0,number=1):
  # Your recursive implementation of the code.
  if new_n==0:
    new_n=n
  if new_n==number or n==0:
    return [n,number]
  if new_n%number==0:
    new_n=new_n//number
    return is_exact(n,new_n,number+1)
  else:
    return 'Not exact!'

