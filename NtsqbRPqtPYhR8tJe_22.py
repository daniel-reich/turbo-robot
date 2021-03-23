"""


A block sequence in three dimensions. We can write a formula for this one:

![Sequence Step 1 - 5](https://edabit-
challenges.s3.amazonaws.com/3d_blocks.png)

Create a function that takes a number (step) as an argument and returns the
amount of blocks in that step.

### Examples

    blocks(1) ➞ 5
    
    blocks(5) ➞ 39
    
    blocks(2) ➞ 12

### Notes

  * Step 0 obviously has to return `0`.
  * The input is always a positive integer.
  * Check the **Resources** tab for a video on finding quadratic sequences.

"""

def blocks(step):
  if step == 0:
    return 0
  return 0.5*step**2 + 5.5*step -1
​
# an**2 +bn + c
# 2a = second difference
# 3a + b = second term - first term
# a + b + c = first term
# sequence = 5,12,20,29,39
# 3a + b = 7
#
# first difference = 7,8,9,10
# second diff = 1 = 2a: a = 0.5
# 3a + b = 7 : 1.5 + b = 7 ....b=5.5
# c = 5 - 5.5 -0.5 = -1

