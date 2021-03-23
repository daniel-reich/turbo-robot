"""


A tank has pure water flowing into it at 10 l/min. The contents of the tank
are kept thoroughly mixed, and the contents flow out at 10 l/min. Salt is
added to the tank at a rate of 0.1 kg/min. Initially, the tank contains 10 kg
of salt in 100 l of water.

Devise a function whose argument is time `t`. The function returns the amount
of salt (kg) left in the tank after `t` minutes rounded to 3 decimal places.

### Examples

    salt(0) ➞ 10.0
    
    salt(5) ➞ 6.459
    
    salt(10) ➞ 4.311
    
    salt(120) ➞ 1.0

### Notes

  * Assume the added salt has a negligible effect on the volume of the liquid in the tank.
  * Keep in mind the amount of salt in the tank is changing continuously.

"""

def salt(t):
  from math import e
​
  salt = eval('1 + 9 * e ** -(0.1*t)')
​
  return round(salt, 3)

