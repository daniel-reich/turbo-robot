"""


Here's an image of four models. Some of the cubes are hidden behind other
cubes. Model one consists of one cube. Model two consists of four cubes, and
so on...

![Stack the Boxes](https://edabit-
challenges.s3.amazonaws.com/stack_the_boxes.png)

Write a function that takes a number `n` and returns the number of stacked
boxes in a model `n` levels high, visible and invisible.

### Examples

    stack_boxes(1) ➞ 1
    
    stack_boxes(2) ➞ 4
    
    stack_boxes(0) ➞ 0

### Notes

Step `n` is a positive integer.

"""

def stack_boxes(n):
  B = n*n
  return B

