"""


The **left shift** operation is similar to **multiplication by powers of two**
, thus, the process is _repetitive_ and can be done _recursively_.

Sample calculation using the left shift operator (`<<`):

    10 << 3 = 10 * 2^3 = 10 * 8 = 80
    -32 << 2 = -32 * 2^2 = -32 * 4 = -128
    5 << 2 = 5 * 2^2 = 5 * 4 = 20

Write a **recursive** function that **mimics** (without the use of **< <**)
the left shift operator and returns the result from the two given integers.

### Examples

    shift_to_left(5, 2) ➞ 20
    
    shift_to_left(10, 3) ➞ 80
    
    shift_to_left(-32, 2) ➞ -128
    
    shift_to_left(-6, 5) ➞ -192
    
    shift_to_left(12, 4) ➞ 192
    
    shift_to_left(46, 6) ➞ 2944

### Notes

  * There will be no negative values for the second parameter `y`.
  * This challenge is more like recreating of the **left shift** operation, thus, **the use of the operator directly** is **prohibited**.
  * You are expected to solve this challenge via **recursion**.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/3xcAQ3CfLAcbEtXys).

"""

def shift_to_left(x, y):
  if y==0:
    return x
  else:
    return 2*shift_to_left(x, y-1)

