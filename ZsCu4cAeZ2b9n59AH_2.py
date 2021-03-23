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

def lost_dog(*lst):
  dogs, res = 0, {}
  
  for i in range(len(lst)):
    if 0 in lst[i]:
      dogs += 1
      k = 'Dog{}'.format(dogs)
      v = 'House ({}) and Room ({})'.format(i + 1, lst[i].index(0) + 1)
      res.update({k: v})
​
  return res if dogs else 'Dog not found!'

