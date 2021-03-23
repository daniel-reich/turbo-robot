"""


Captain Obvious is asked to implement a simple function that given two decimal
numbers `A` and `B` returns their sum.

" _Easy one!_ " he thinks, but soon he discovers that his function fails over
the fifty percent of given test cases! He suspects the test cases are wrong,
but his calculator is saying they're correct! What's happening?

Can you help Captain Obvious to debug his function and solve the exercise?

### Examples

    float_sum(0.3, 0.7) ➞ 1
    
    float_sum(0.35, 0.75) ➞ 1.1
    
    float_sum(1.234, 5.6789) ➞ 6.9129

### Notes

  * Given numbers can be either integer or float with 1 up to 6 decimals.
  * Don't round results!
  * Bonus: Can you resolve it using a simple math expression instead of a built-in method?

"""

def float_sum(A, B):
  return (A * 1000000 + B *1000000)/1000000

