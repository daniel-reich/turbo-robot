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
  num, blocks = 5, []
  lst = [i for i in range(step)]
  if not step:
    return 0
  for i in lst:
    if i == 0:
      blocks.append(num)
    else:
      if i > 0:
        blocks.append(((num + blocks[i-1]) + i)+1)
  return blocks[-1]

