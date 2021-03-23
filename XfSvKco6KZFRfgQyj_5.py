"""


A train has a maximum capacity of `n` passengers overall, which means each
carriage's capacity will share an equal proportion of the maximum capacity.

Create a function which returns the **index** of the first carriage which
holds **50% or less** of its maximum capacity. If no such carriage exists,
return `-1`.

### Worked Example

    find_a_seat(200, [35, 23, 18, 10, 40]) ➞ 2
    
    # There are 5 carriages which each have a maximum capacity of 40 (200 / 5 = 40).
    # Index 0's carriage is too full (35 is 87.5% of the maximum).
    # Index 1's carriage is too full (23 is 57.5% of the maximum).
    # Index 2's carriage is good enough (18 is 45% of the maximum).
    # Return 2.

### Examples

    find_a_seat(20, [3, 5, 4, 2]) ➞ 3
    
    find_a_seat(1000, [50, 20, 80, 90, 100, 60, 30, 50, 80, 60]) ➞ 0
    
    find_a_seat(200, [35, 23, 40, 21, 38]) ➞ -1

### Notes

  * This means if a train can hold **200** passengers, and has **5** carriages, then that means each carriage can hold a maximum of **40** passengers each.
  * All carriage numbers will be positive integers, which will be able to divide evenly.
  * Remember to return `-1` if no carriage is empty enough.

"""

class Train:
  class Carriage:
    percentage = lambda used, cap: used/cap*100
    def __init__(self, capacity, used):
      self.c = capacity
      self.u = used
      self.perc = Train.Carriage.percentage(self.u, self.c)
  
  def __init__(self, capacity):
    self.capacity = capacity
    self.car = []
  
  determine_car_cap = lambda cap, num_of_cars: cap // num_of_cars
  
  def add_carriage(self, car_used, num_of_cars):
    
    car_cap = Train.determine_car_cap(self.capacity, num_of_cars)
    self.car.append(Train.Carriage(car_cap, car_used))
​
def find_a_seat(n, lst):
  
  train = Train(n)
  
  for carr in lst:
    train.add_carriage(carr, len(lst))
# print(train.car[0].c, train.car[0].u, train.car[0].perc)
  for n in range(len(train.car)):
    if train.car[n].perc <= 50:
      return n
  
  return -1

