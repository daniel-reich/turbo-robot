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
  if n == 1:
    return 5
  if n == 2:
    return 100
  current_position = 2
  little_num = 5
  big_num = 100
  for i in range(2, n + 1):
    little_num += 1
    current_position += 1
    if current_position == n:
      return little_num
    big_num *= 2
    current_position += 1
    if current_position == n:
      return big_num

