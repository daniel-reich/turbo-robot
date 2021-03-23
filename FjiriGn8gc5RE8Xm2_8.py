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
    pct = passengers * .05
    fuel_usage = (1 + pct) * fuel_usage
    if air_con:
        fuel_usage = fuel_usage * 1.1
    return round(100*fuel/fuel_usage,1)

