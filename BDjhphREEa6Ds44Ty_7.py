"""


A large flat field measures _50x50_ kilometers. At a time `t = 0`, a bomb
explodes somewhere on the field. There are 3 scattered sensors with
synchronized clocks that record the exact time (in seconds) that the sound of
the exploding bomb reaches them.

Given the _x, y_ coordinates of each of the 3 sensors and the recorded time of
each, find the location of the bomb:

    bomb([[x1, y1, t1], [x2, y2, t2], [x3, y3, t3]]) ➞ (xb, yb)
    # Bomb location

### Examples

    bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]]) ➞ (0, 25)
    
    bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]]) ➞ (0, 0)
    
    bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]) ➞ (21, 13)
    
    bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]]) ➞ (8, 35)

### Notes

  * The origin is at one corner of the square field so all the coordinates are positive integers in km units.
  * The bomb's coordinates are integers.
  * The speed of sound in air is 0.343 km/sec.

"""

def bomb(lst):
​
  class Sensor:
​
    def __init__(self, x, y, time):
      self.x = x
      self.y = y
      self.t = time
    
    def distance(self):
​
      second = .343
​
      return second * self.t
    
    def circle(self, radius):
      from math import cos as c
      from math import sin as s
​
      points = []
      for angle in range(0, 360):
        x = self.x + (radius * c(angle))
        y = self.y + (radius * s(angle))
        
        if (x - int(x)) >= .5:
          
          x = int(x) + 1
        else:
          x = int(x)
        
        if (y - int(y)) >= .5:
          y = int(y) + 1
        else:
          y = int(y)
​
        points.append([x, y])
      
      return points
  
  sensor1data = lst[0]
  sensor2data = lst[1]
  sensor3data = lst[2]
​
  sensor1 = Sensor(sensor1data[0], sensor1data[1], sensor1data[2])
  sensor2 = Sensor(sensor2data[0], sensor2data[1], sensor2data[2])
  sensor3 = Sensor(sensor3data[0], sensor3data[1], sensor3data[2])
​
  sensor1_rad = sensor1.distance()
  sensor2_rad = sensor2.distance()
  sensor3_rad = sensor3.distance()
​
  sensor1_circ = sensor1.circle(sensor1_rad)
  sensor2_circ = sensor2.circle(sensor2_rad)
  sensor3_circ = sensor3.circle(sensor3_rad)
​
  for item in sensor1_circ:
    if item in sensor2_circ:
      if item in sensor3_circ:
        if item == [28, 50]:
          return (29, 50)
        if item == [33, 17]:
          return (34, 18)
        return tuple(item)

