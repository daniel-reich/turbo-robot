"""


Write a function that returns the **least common multiple (LCM)** of two
integers.

### Examples

    lcm(9, 18) ➞ 18
    
    lcm(8, 5) ➞ 40
    
    lcm(17, 11) ➞ 187

### Notes

  * Both values will be positive.
  * The **LCM** is the smallest integer that is divisible by both numbers such that the remainder is zero.

"""

def lcm(n1, n2):
  n_multiple = set()
  i = 1
  while True:
      if n1*i not in n_multiple:
          n_multiple.add(n1*i)
      else:
          return n1*i
​
      if n2*i not in n_multiple:
          n_multiple.add(n2*i)
      else:
          return n2*i
​
      i += 1

