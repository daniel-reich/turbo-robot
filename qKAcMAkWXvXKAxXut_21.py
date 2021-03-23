"""


Lets assume for the purposes of this challenge that for every _layer of
fabric_ you wear when it's cold outside (coats, cardigans, etc), the
temperature increases by a _tenth of the total_.

Given `n` number of layers and a given temperature, return the temperature
inside of all those warm fuzzy layers. Round to the nearest _tenth_ of a
degree.

    calc_bundled_temp(2, "10*C") ➞ "12.1*C"
    # 10 * 1.1 = 11
    # 11 * 1.1 = 12.1

### Examples

    calc_bundled_temp(1, "2*C") ➞ "2.2*C"
    
    calc_bundled_temp(4, "6*C") ➞ "8.8*C"
    
    calc_bundled_temp(20, "4*C") ➞ "26.9*C"

### Notes

  * The temperature will be given in celsius and as a string.
  * Note that the degrees sign is given as an asterisk.

"""

import re
def calc_bundled_temp(n, temp):
  temp = int(re.sub(r'\D+','',temp))
  def new_temp(n,temp):
    return "{}*C".format(str(round(temp,1))) if n == 0 else new_temp(n-1,(.1 * temp) + temp)
  return new_temp(n,temp)

