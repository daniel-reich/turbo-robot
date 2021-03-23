"""


Create a function that returns `True` if the combined weight of a car `car`
and the weight of the passengers `p` in the car is less than the maximum
weight `max_weight` the car is allowed to carry. Otherwise, return `False`.
The weight of the car and the weight of the passengers are given in pounds.
The maximum weight is given in kilograms.

### Examples

    weight_allowed(3000, [150, 201, 75, 88, 195], 1700) ➞ True
    
    weight_allowed(3200, [220, 101, 115, 228, 15], 1700) ➞ False
    
    weight_allowed(2900, [225, 171, 300, 274, 191], 1850) ➞ True

### Notes

1 pound = 0.453592 kilogram

"""

def weight_allowed(car, p, max_weight):
  
  Total_A = 0
  
  for x in p:
    Total_A += x
    
  Total_A += car
  
  Total_A *= 0.453592
  Total_B = max_weight
  
  if (Total_A <= Total_B):
    return True
  else:
    return False

