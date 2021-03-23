"""


Create a function that takes two numbers as arguments and return the LCM of
the two numbers.

### Examples

    lcm(3, 5) ➞ 15
    
    lcm(14, 28) ➞ 28
    
    lcm(4, 6) ➞ 12

### Notes

  * Don't forget to return the result.
  * You may want to use the GCD function to make this a little easier.
  * LCM stands for least common multiple, the smallest multiple of both integers.

"""

def lcm(x, y):
  if x > y:
    greater = x
  else:
    greater = y
​
  while(True):
    if((greater % x == 0) and (greater % y == 0)):
      lcm = greater
      break
    greater += 1
​
  return lcm

