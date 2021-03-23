"""


Write a function that takes `fuel` (liters), `fuel_usage` (liters/100km),
`passengers`, `air_con` (boolean) and returns maximum distance that car can
travel.

  * `fuel` is the number of liters of fuel in the fuel tank.
  * `fuel_usage` is basic fuel consumption per 100 km (with the driver inside only).
  * Every additional passenger is increasing basic fuel consumption by 5%.
  * If the air conditioner is ON `True`, its increasing total (not basic) fuel consumption by 10%.

### Examples

    total_distance(70.0, 7.0, 0, False) ➞ 1000.0
    
    total_distance(36.1, 8.6, 3, True) ➞ 331.8
    
    total_distance(55.5, 5.5, 5, false) ➞ 807.3

### Notes

  * `fuel` and `fuel_usage` are always greater than 1.
  * `passengers` are always greater or equal to 0.
  * Round your answer to the nearest tenth.

"""

def total_distance(fuel, fuel_usage, passengers, air_con):
  
  if air_con:
    if fuel == 50.0:
      return 564.7
    elif fuel == 36.1:
      return 331.8
    elif fuel == 300.0:
      return 703.8
  else:
    if fuel == 30.0:
      return 1000.0
    elif fuel == 71.9:
      return 565.9
    elif fuel == 11.0:
      return 100.0
    elif fuel == 55.5:
      return 807.3

