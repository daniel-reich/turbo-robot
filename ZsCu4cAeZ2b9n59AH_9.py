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

def lost_dog(*alist):
    newlist = {}
    prefix = 'Dog'
    dog_count = 1
    for i in range(len(alist)):
        house = alist[i]
        for j in range(len(house)):
            if house[j] == 0:
                newlist['Dog{}'.format(dog_count)] = 'House ({}) and Room ({})'.format(i+1,j+1)
                dog_count += 1
                break
    if len(newlist) == 0:
        return 'Dog not found!'
    else:
        return newlist

