"""


A typical car can hold **four passengers** and **one driver** , allowing
**five people** to travel around. Given `n` number of people, return how many
cars are needed to seat everyone comfortably.

### Examples

    cars_needed(5) ➞ 1
    
    cars_needed(11) ➞ 3
    
    cars_needed(0) ➞ 0

### Notes

It's likely there will be a few people left over and some cars won't be filled
to max capacity.

"""

def cars_needed(n):
  cars, extra = divmod(n, 5)
  return cars + 1 if extra else cars

