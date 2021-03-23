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
  if n == 0:
    return 0
  elif n <= 5:
    return 1
  elif n > 5:
    car = n // 5
    if n%5 == 0:
      return car
    elif n%5 != 0 :
      return car + 1
  else:
    return "Whoops!"

