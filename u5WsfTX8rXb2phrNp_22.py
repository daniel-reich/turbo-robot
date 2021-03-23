"""


Kinetic energy can be calculated with the following formula:

![KE = 1/2mv²](https://edabit-challenges.s3.amazonaws.com/kenen.png)

  *  **m** is mass in kg
  *  **v** is velocity in m/s
  *  **KE** is kinetic energy in J

Return the Kinetic Energy in _Joules_ , given the mass and velocity. For the
purposes of this challenge, **round answers to the nearest integer.**

###  Examples

    calc_kinetic_energy(60, 3) ➞ 270
    
    calc_kinetic_energy(45, 10) ➞ 2250
    
    calc_kinetic_energy(63.5, 7.35) ➞ 1715

### Notes

Expect only positive numbers for inputs.

"""

def calc_kinetic_energy(m, v):
  return round(0.5 * m * v**2, 0)

