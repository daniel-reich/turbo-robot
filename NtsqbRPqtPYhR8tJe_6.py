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
  if step == 0: return 0
  sum = 5
  increase_by = 6
  for i in range(0, step-1):
    increase_by = increase_by + 1
    sum = sum + increase_by
  return sum

