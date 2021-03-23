"""


  * `0` represents the dog.
  * Each list represents a house and each `1` represents an empty room.
  * Return the house and the room where it is located, there can be only one dog lost per building.

### Examples

    lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
    ➞ "Dog not found!"
    
    lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
    ➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}
    
    lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
    ➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)", "Dog4": "House (4) and Room (3)"}

### Notes

Check the **Resources** if you're stuck.

"""

def lost_dog(*neighborhood):
  dogs = {}
  n_dog = 0
  for x, house in enumerate(neighborhood, start=1):
    for y, room in enumerate(house, start=1):
      if not room:
        n_dog += 1
        k = 'Dog{}'.format(n_dog)
        v = 'House ({}) and Room ({})'.format(x, y)
        dogs[k] = v
  return dogs or 'Dog not found!'

