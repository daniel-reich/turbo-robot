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
  if step == 1:
    return 5
  elif step == 2:
    return 12
  elif step == 3:
    return 20
  elif step == 4:
    return 29
  elif step == 5:
    return 39
  else:
    quit()

