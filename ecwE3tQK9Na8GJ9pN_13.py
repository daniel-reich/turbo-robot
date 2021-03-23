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
  res = []
  for i in range(n):
    if not i % 2:
      res.append(5 + i // 2)
    elif i == 1:
      res.append(100)
    else:
      res.append(res[i - 2] * 2)
  return res[-1]

