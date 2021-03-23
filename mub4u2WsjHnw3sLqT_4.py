"""


Create a function which takes a parameter `n` and returns a function such that
it, when called `n` times, returns the string `"edabit"`.

### Examples

    lambda_depth(0) ➞ "edabit"
    
    lambda_depth(1)() ➞ "edabit"
    
    lambda_depth(2)()() ➞ "edabit"
    
    type(lambda_depth(2)()) ➞ <class: "function">

### Notes

  * `num` will always be a non-negative integer.
  * If `num == 0`, return `"edabit"`.
  * If `num > 0`, return a function.
  * All non-example test cases come in two forms: checking whether `lambda_depth(k)`, after being called `k` times, returns a string, and checking whether `lambda_depth(k)` returns a function.

"""

def lambda_depth(num=0):
  if num > 0:
    lambda_depth.n = 0
    lambda_depth.g = num
​
  if lambda_depth.n == lambda_depth.g:
    lambda_depth.n = 0
    return "edabit"
  else : 
    lambda_depth.n += 1
    return lambda_depth
    
lambda_depth.n = 0
lambda_depth.g = 0

