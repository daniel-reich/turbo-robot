"""


You are given a list `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the `asteroids` after all collisions. If two `asteroids`
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

### Examples

    asteroid_collision([-2, -1, 1, 2]) ➞ [-2, -1, 1, 2]
    
    asteroid_collision([-2, 1, 1, -2]) ➞ [-2, -2]
    
    asteroid_collision([1, 1, -2, -2]) ➞ [-2, -2]
    
    asteroid_collision([10, 2, -5]) ➞ [10]
    
    asteroid_collision([8, -8]) ➞ []

### Notes

BONUS: Use only one loop (either `for` or `while`).

"""

def asteroid_collision(asteroids):
  new=asteroids.copy()
​
  x=new.pop(0)
  out=[]
​
  while True:
    old=0
    if len(out)>0:old=out.pop()
    if  old >0 and x <0: # different sign
      if abs(old)==abs(x):x,old=0,0
      if abs(old)>abs(x):x=old
    else:
      if old!=0: out.append(old)
      if x!=0: out.append(x)
      if len(new)==0: return out
      x=new.pop(0)

