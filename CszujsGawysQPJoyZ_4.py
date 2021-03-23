"""


You're working for Jaffar in the newest game of Prince of Persia. The prince
is coming to get the princess and you have to stop him. He's entering the
castle on a horse, don't ask me why he's riding a horse... he just is!

You're standing next to the cannon and you have to check if the aim / velocity
/ height is ok for hitting the prince on his horse.

Your function will get four values / circumstances:

  1. Velocity
  2. Angle
  3. Height
  4. Distance to the prince

With the formula of **Ballistic Trajectory** you'll be able to calculate the
distance the cannonball is gonna travel for impact. You don't need to apply
rounding.

The complete formula is found in the **Resources** section. Computations are
based on the acceleration of gravity on the earth's surface (9.81 m/s/s),
atmospheric drag is neglected. The chance of hitting the prince / his horse is
plus or minus 0.5m.

### Examples

    hit_prince(10, 10, 10, 16) ➞ True
    
    hit_prince(20, 45, 0, 45) ➞ False
    
    hit_prince(5, 45, 10, 6) ➞ True

![Ballistic Trajectory](https://edabit-
challenges.s3.amazonaws.com/trajectory-2D.gif)

### Notes

  * No actual princes / horses are harmed during the making of this challenge.
  * All the inputs are correct. 0 > Angle < 90, and so on.
  * Values will be in meters per second / degrees / meters.

"""

import math
def hit_prince(vo, th, yo, ds):
  vxo = vo * math.cos(th*3.14/180)
  vyo = vo * math.sin(th*3.14/180)
  g=9.81
  trise = vyo/g 
  h=yo + vyo*trise - 0.5*g*trise**2
  tfall=  (2*h/g)**(0.5)
  r=(trise+tfall)*vxo
  return abs(r-ds)<0.5

