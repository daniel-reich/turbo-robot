"""


Mary wants to run a 25-mile marathon. When she attempts to sign up for the
marathon, she notices the sign-up sheet doesn't directly state the marathon's
length. Instead, the marathon's length is listed in small, different portions.
Help Mary find out how long the marathon actually is.

Return `True` if the marathon is 25 miles long, otherwise, return `False`.

### Examples

    marathon_distance([1, 2, 3, 4]) ➞ False
    
    marathon_distance([1, 9, 5, 8, 2]) ➞ True
    
    marathon_distance([-6, 15, 4]) ➞ True

### Notes

  * Items in the list will always be integers.
  * Items in the list may be negative or positive, but since negative distance isn't possible, find a way to convert negative integers into positive integers.
  * Return `False` if the arguments are empty or not provided.

"""

def marathon_distance(d):
  return sum(map(abs, d)) == 25

