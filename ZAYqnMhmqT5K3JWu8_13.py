"""


A vehicle needs 10 times the amount of fuel than the distance it travels.
However, it must always carry a minimum of 100 fuel before setting off.

Create a function which calculates the amount of fuel it needs, given the
distance.

### Examples

    calculate_fuel(15) ➞ 150
    
    calculate_fuel(23.5) ➞ 235
    
    calculate_fuel(3) ➞ 100

### Notes

  * Distance will be a number greater than zero.
  * Return 100 if the calculated fuel turns out to be less than 100.

"""

def calculate_fuel(n):
  fuel = n * 10
  if fuel < 100:
    return 100
  else:
    return fuel

