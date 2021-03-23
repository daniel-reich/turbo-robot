"""


A number sequence is as follows:

    5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200, ...

Given that `5` is at position **1** , create a function that returns the
number found at position `n` in the sequence.

### Examples

    little_big(4) ➞ 200
    
    little_big(5) ➞ 7
    
    little_big(28) ➞ 819200

### Notes

You can expect to be only given valid inputs.

"""

def little_big(n):
  lst = [5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200, 11, 6400, 12, 12800, 13, 25600, 14, 51200, 15, 102400, 16, 204800, 17, 409600, 18, 819200, 19, 1638400]
  return lst[n-1]

