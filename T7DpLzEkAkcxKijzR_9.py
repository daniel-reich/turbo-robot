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
    capacity = 5
​
    # Full cars is equal to amount of passengers / capacity of cars, rounded
    # to full numbers
    cars_full = n // capacity
​
    # If there are any leftover passengers that couldn't fit in full cars,
    # return the amount of full cars plus one extra car
    if n % capacity:
        return cars_full + 1
    else:
        return cars_full

