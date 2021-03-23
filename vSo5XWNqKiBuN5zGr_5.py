"""


Create a function that returns the **integral** part from the result of a
division between two numbers. This process of division can be achieved via
**repetitive subtraction** , thus, it can be done **recursively**.

### Examples

    divide(10, 2) ➞ 5
    
    divide(-51, -4) ➞ 12
    
    divide(3, 9) ➞ 0
    
    divide(-21, 5) ➞ -4
    
    divide(1024, 7) ➞ 146
    
    divide(273, -6) ➞ -45

### Notes

  * There will be no **zero-values** for the _divisor_.
  * You're expected to solve this challenge using a **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.

"""

def divid(x, y,count):
  # Your recursive solution here.
  if abs(x)<abs(y):
    if x*y>=0:
      return count
    else:
      return -count
  elif x*y>0:
    x=x-y
    count=count+1
    return divid(x,y,count)
  elif x*y<0:
    x=x+y
    count=count+1
    return divid(x,y,count)
def divide(x,y):
  return divid(x,y,0)

